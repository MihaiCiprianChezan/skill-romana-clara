#!/usr/bin/env python3
"""Mechanical checks for romana-clara (references/verificare.md, sections A, B0, B, C, D1).

Runs only the checks that need no judgment, plus a few heuristics that are
reported as candidates ("de verificat"). Everything else in verificare.md
(agents, integrity, structure) still needs a human or the model.

Usage:
    python verifica.py FILE [FILE ...]        # report in Romanian, G format
    python verifica.py --json FILE            # machine-readable
    python verifica.py -                      # read stdin

Exit code: 0 no findings, 1 findings, 2 usage or read error.
Standard library only. Python 3.8+.
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass

RO_UPPER = "A-ZĂÂÎȘȚŞŢ"
WORD = r"[\wăâîșțşţĂÂÎȘȚŞŢ]"


@dataclass
class Finding:
    rule: str          # rule number from SKILL.md, or a table reference
    tier: str          # "N", "S", or "F"
    line: int
    text: str          # offending text
    fix: str           # suggested fix, or "" when the fix needs judgment
    note: str          # why
    candidate: bool    # True: heuristic hit, a human must confirm


# ---------------------------------------------------------------------------
# Masking: code is untouchable (SKILL.md, Intangibile) and counts as one word
# (Rule 8.1). Replace it with same-length filler so offsets and lines survive.
# ---------------------------------------------------------------------------

def mask(text):
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))

    text = re.sub(r"^(```|~~~).*?^\1[^\n]*$", blank, text, flags=re.M | re.S)

    def inline(m):
        n = len(m.group(0))
        return ("COD" + " " * n)[:n] if n >= 3 else " " * n

    text = re.sub(r"`[^`\n]+`", inline, text)
    text = re.sub(r"https?://\S+", lambda m: " " * len(m.group(0)), text)
    text = re.sub(r"&[a-zA-Z]+;|&#\d+;", lambda m: " " * len(m.group(0)), text)
    return text


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


# ---------------------------------------------------------------------------
# Section A — pattern checks
# ---------------------------------------------------------------------------

# (id, regex, rule, tier, fix, note, candidate)
PATTERNS = [
    ("A3", r"\b(sînt|sîntem|sînteți|cînd|rîu|mîine)\b", "7.3", "N",
     "sunt / când / râu / mâine", "grafie cu î dinainte de 1993", False),
    ("A4", r";", "3.7", "S",
     "două fraze", "punct și virgulă între enunțuri independente", False),
    ("A5", r"\betc\.|ș\.a\.m\.d\.", "7.12", "S",
     "și altele", "listă deschisă; numiți elementele doar dacă sursa le dă", False),
    ("A5b", r"(?<!\w)(i\.e\.|e\.g\.|cf\.|viz\.)", "7.14", "S",
     "adică / de exemplu / compară / vezi", "abreviere latină", False),
    ("A6", r"\bși/sau\b", "inlocuiri.md §9", "S",
     "X, Y sau ambele", "nu alegeți doar unul — schimbă sensul", False),
    ("A7", r"\bdin punct de vedere (al|a)\b", "7.7", "S",
     "din punctul de vedere al", "articol lipsă", False),
    ("A8", r"\bca și (?=c)\w+", "7.6", "S",
     "ca", "și inserat contra cacofoniei; păstrați-l într-o comparație reală", True),
    ("A9", r"\bdatorită (pierderii|prăbușirii|eșecului|întârzierii|defecțiunii|erorii|"
           r"accidentului|avariei|lipsei|neglijenței)\b", "7.5", "S",
     "din cauza", "datorită doar pentru cauze cu efect pozitiv", False),
    ("A11", r"\bsa (\w+(at|ut|it|ât|ăt|is|us))\b", "7.13", "S",
     "s-a", "verb la perfect compus fără cratimă", False),
    ("A11b", r"\bva (\w+(at|ut|it|ât|ăt|is|us))\b", "7.13", "S",
     "v-a", "verb la perfect compus fără cratimă", False),
    ("A12", r"\b(într|dintr|printr)( |)(un|o|una|unul)\b", "7.13", "S",
     "într-un / dintr-o / printr-un", "cratimă lipsă", False),
    ("A12b", r"\bintr-(un|o|una|unul)\b", "7.13", "S",
     "într-", "diacritică lipsă", False),
    ("A13", r"\bde a (lungul|latul)\b", "7.13", "S",
     "de-a lungul / de-a latul", "cratimă lipsă", False),
    # Self-check step 3 and section C
    ("C1", r"\bse (va|vor) \w+", "2.2", "S",
     "", "cine face acțiunea? Numiți-l doar dacă textul îl dă", True),
    ("C4", r"\bavând în vedere( faptul că)?", "2.5", "F",
     "întrucât", "gerunziu: subiectul trebuie să fie clar și alăturat", True),
    ("C4b", r"\bîn vederea\b", "inlocuiri.md §3", "S",
     "pentru / pentru a", "construcție nominală", False),
    ("C5", r"\burmează (a fi|să se) \w+", "2.8", "S",
     "viitorul simplu sau prezentul", "perifrază", False),
    ("C6b", r"\bar trebui\b", "2.12", "F",
     "", "obligație (trebuie) sau recomandare? Nu schimbați mecanic", True),
    ("C3", r"\b(efectuarea|realizarea|asigurarea|efectuării|realizării|asigurării)\b", "2.3", "N",
     "verbul corespunzător", "substantiv în loc de verb", True),
    ("D5", r"\b(merită menționat faptul că|este important de reținut că|trebuie subliniat că|"
           r"pur și simplu|fără efort|în mod fluid|de ultimă generație|extrem de rapid|"
           r"soluție de tip)\b", "inlocuiri.md §8", "S",
     "ștergeți", "nu poartă niciun fapt", False),
]

CEDILLA = {"ş": "ș", "Ş": "Ș", "ţ": "ț", "Ţ": "Ț"}

MISSING_DIACRITICS = {
    "fara": "fără", "insa": "însă", "desi": "deși", "daca": "dacă", "dupa": "după",
    "catre": "către", "astazi": "astăzi", "stiu": "știu", "acestia": "aceștia",
}

# A10: `care` as direct object needs `pe`. Only flag the unambiguous shape:
# a 1st/2nd-person auxiliary (care cannot be its subject) plus an object clitic.
A10_RE = re.compile(
    r"(?<!\bpe )\bcare\s+((?:\S+\s+){0,2}\S*)", re.I)
A10_PERSON = re.compile(r"(?:^|[\s-])(am|ai|ați|aţi)(?=$|[\s-])", re.I)
A10_CLITIC = re.compile(r"(-o\b|(?:^|\s)l-|(?:^|\s)îl\s|(?:^|\s)o\s)", re.I)


def check_patterns(masked, findings):
    for m in re.finditer("|".join(re.escape(c) for c in CEDILLA), masked):
        ch = m.group(0)
        start = masked.rfind(" ", 0, m.start()) + 1
        end_m = re.search(r"[\s.,;:!?)\]]|$", masked[m.end():])
        word = masked[start:m.end() + end_m.start()]
        findings.append(Finding("7.2", "N", line_of(masked, m.start()), word,
                                word.translate(str.maketrans(CEDILLA)),
                                f"cedilă {ch} (U+{ord(ch):04X}) în loc de virgulă", False))

    words = re.findall(WORD + "+", masked)
    has_diacritics = re.search(r"[ăâîșțşţĂÂÎȘȚŞŢ]", masked) is not None
    if not has_diacritics and len(words) >= 20:
        findings.append(Finding("7.1", "N", 1, "(tot textul)", "",
                                "textul nu are nicio diacritică", False))
    else:
        for bad, good in MISSING_DIACRITICS.items():
            for m in re.finditer(rf"\b{bad}\b", masked, re.I):
                findings.append(Finding("7.1", "N", line_of(masked, m.start()),
                                        m.group(0), good, "diacritică lipsă", False))

    for pid, rx, rule, tier, fix, note, cand in PATTERNS:
        for m in re.finditer(rx, masked, re.I):
            findings.append(Finding(rule, tier, line_of(masked, m.start()),
                                    m.group(0).strip(), fix, note, cand))

    for m in A10_RE.finditer(masked):
        window = m.group(1)
        if A10_PERSON.search(window) and A10_CLITIC.search(" " + window + " "):
            findings.append(Finding("7.4", "N", line_of(masked, m.start()),
                                    ("care " + window).strip(), "pe care …",
                                    "care complement direct fără pe", True))


# ---------------------------------------------------------------------------
# Sentences and word counting (SKILL.md Section 8)
# ---------------------------------------------------------------------------

ABBREV = ["art.", "alin.", "lit.", "nr.", "pct.", "str.", "tel.", "ex.", "dvs.", "dl.",
          "dna.", "d.", "prof.", "dr.", "ing.", "i.e.", "e.g.",
          "cf.", "viz.", "p.", "pp.", "vol.", "fig.", "cap.", "sec."]


def sentences(masked):
    """Yield (line, sentence) pairs. Headings, list items and table cells are
    separate units; a line ending in ':' ends a sentence (Rule 8.7)."""
    units = []
    para, para_line = [], 0

    def flush():
        nonlocal para
        if para:
            units.append((para_line, " ".join(para)))
        para = []

    for i, raw in enumerate(masked.split("\n"), 1):
        line = raw.strip()
        line = re.sub(r"^>\s?", "", line)
        label = re.match(r"^\*\*([^*]+:)\*\*\s+(.+)$", line)
        if label:
            # A bold lead-in label is not part of the sentence it introduces.
            flush()
            units.append((i, label.group(1)))
            line = label.group(2)
        if not line or re.fullmatch(r"[-|: ]+", line) or line in ("---", "***"):
            flush()
            continue
        if line.startswith("#"):
            flush()
            units.append((i, line.lstrip("# ")))
            continue
        if line.startswith("|"):
            flush()
            for cell in line.strip("|").split("|"):
                if cell.strip():
                    units.append((i, cell.strip()))
            continue
        item = re.match(r"^([-*+]|\d+[.)])\s+(.*)", line)
        if item:
            flush()
            para_line = i
            para = [item.group(2)]
        else:
            if not para:
                para_line = i
            para.append(line)
        if line.endswith(":"):
            flush()
    flush()

    out = []
    for line, unit in units:
        unit = re.sub(r"\*\*|__|(?<!\w)[*_](?!\s)|(?<!\s)[*_](?!\w)", "", unit)
        protected = unit
        for ab in ABBREV:
            protected = re.sub(r"(?i)(?<!\w)" + re.escape(ab), lambda m: m.group(0).replace(".", "\x00"),
                               protected)
        protected = re.sub(r"(\d)\.(\d)", "\\1\x00\\2", protected)
        parts = re.split(rf"(?<=[.!?…])\s+(?=[{RO_UPPER}„\"(0-9])", protected)
        for p in parts:
            p = p.replace("\x00", ".").strip()
            if p:
                out.append((line, p))
    return out


STOP = set("""a al ai ale ăla aia la în pe de din cu și sau dar ori că să se nu mai
este sunt e fi fost a fost au am ai ați va vor ar care ce cine cum când unde dacă
pentru prin spre între după până fără sub peste către lângă despre asupra
un o unui unei unor niște acest această aceste acești acel acea acei acele
acestui acestei acestor acelui acelei acelor lui ei lor le li îl îi îmi mi ne
vă v-a s-a l-a i-a eu tu el ea noi voi ele său sa săi sale meu mea mei mele
fiecare fiecărei fiecărui oricare cărei căror cărui""".split())

UNIT_JOIN = re.compile(
    r"\b(\d[\d.,]*)\s+(?:(de)\s+)?(%|[a-zăâîșț]+)\b", re.I)
CITATION = re.compile(
    r"\bart\.\s*\d+(\s+alin\.\s*\(\d+\))?(\s+lit\.\s*[a-z]\))?"
    r"(\s+din\s+(Legea|OUG|HG|OG|Ordonanța|Hotărârea)\s+nr\.\s*\d+/\d+)?"
    r"|\b(Legea|OUG|HG|OG)\s+nr\.\s*\d+/\d+", re.I)


def count_words(sentence):
    s = CITATION.sub("CIT", sentence)

    def unit(m):
        word = m.group(3)
        if word.lower() in STOP:
            return m.group(0)
        return "NUM"
    s = UNIT_JOIN.sub(unit, s)
    tokens = re.findall(r"[\wăâîșțşţĂÂÎȘȚŞŢ%][\wăâîșțşţĂÂÎȘȚŞŢ%'’-]*", s)

    # Rule 8.5: a run of capitalized words (not sentence-initial) is one name.
    count, i = 0, 0
    while i < len(tokens):
        t = tokens[i]
        if i > 0 and t[:1].isupper() and t not in ("NUM", "CIT", "COD"):
            j = i + 1
            while j < len(tokens) and (
                    tokens[j][:1].isupper() or
                    (tokens[j] in ("de", "pentru", "și") and j + 1 < len(tokens)
                     and tokens[j + 1][:1].isupper())):
                j += 1
            count += 1
            i = j
            continue
        count += 1
        i += 1
    return count


# ---------------------------------------------------------------------------
# Section B0 — density heuristics
# ---------------------------------------------------------------------------

NOMINAL_END = re.compile(
    r"^\w{3,}(are|area|ării|ere|erea|erii|ire|irea|irii|ție|ția|ției)$", re.I)
NOT_NOMINAL = set("""care oricare fiecare vreunul mare pare tare are rare clare sare
soare floare doare ziare pare lunare solare necesare similare militare populare
sanitare elementare particulare regulare voluntare avere vedere subțire fire
situație situația situației funcție funcția funcției poziție poziția poziției direcție direcția direcției
secție secția secției lecție lecția lecției ediție ediția ediției porție stație
stația stației națiune""".split())

GEN_ENDING = re.compile(r"\w{3,}(ii|ei|lor|ului)$", re.I)
GEN_STOP = set("""acestei acelei acestor acelor fiecărei oricărei cărei căror cărui
unei unor lui ei lor trei mei tăi săi noștri voștri""".split())


def nominal_hits(sentence):
    words = re.findall(WORD + "+", sentence)
    return [w for w in words if NOMINAL_END.match(w) and w.lower() not in NOT_NOMINAL]


def cascade(sentence):
    """Longest chain of noun links: adjacency genitive (X Y-ii), `de` + noun,
    or genitive article + genitive noun. Returns (links, text)."""
    toks = re.findall(WORD + "+", sentence)
    best, best_span = 0, (0, 0)
    i = 0
    while i < len(toks):
        if toks[i].lower() in STOP:
            i += 1
            continue
        links, j = 0, i
        while True:
            nxt = toks[j + 1] if j + 1 < len(toks) else None
            if nxt is None:
                break
            low = nxt.lower()
            if low in ("de",) and j + 2 < len(toks) and toks[j + 2].lower() not in STOP \
                    and not toks[j + 2][0].isdigit():
                links, j = links + 1, j + 2
            elif low in ("a", "al", "ai", "ale") and j + 2 < len(toks):
                k = j + 2
                if toks[k].lower() in ("unei", "unor") and k + 1 < len(toks):
                    k += 1
                if GEN_ENDING.match(toks[k]) and toks[k].lower() not in GEN_STOP:
                    links, j = links + 1, k
                else:
                    break
            elif GEN_ENDING.match(nxt) and low not in GEN_STOP and low not in STOP:
                links, j = links + 1, j + 1
            else:
                break
        if links > best:
            best, best_span = links, (i, j)
        i = max(i + 1, j if links else i + 1)
    a, b = best_span
    return best, " ".join(toks[a:b + 1])


def check_sentences(masked, findings, stats):
    counts = []
    for line, s in sentences(masked):
        n = count_words(s)
        if n < 2:
            continue
        counts.append((n, line, s))
        if n > 20:
            short = s if len(s) <= 90 else s[:87] + "…"
            band = "peste 25: plafon descriptiv și procedural" if n > 25 else \
                "peste 20: plafonul procedural (descriptiv: 25)"
            findings.append(Finding("4.1 / 5.1", "S", line, short, "împărțiți fraza",
                                    f"{n} cuvinte — {band}", n <= 25))
        hits = nominal_hits(s)
        if len(hits) > 1:
            findings.append(Finding("2.10", "S", line, ", ".join(hits), "",
                                    f"{len(hits)} substantive verbale într-o frază "
                                    "(euristic: numărați doar cele derivate din verbe)", True))
        links, chain = cascade(s)
        if links >= 3:
            findings.append(Finding("2.11", "S", line, chain,
                                    "transformați substantivul-cap în verb",
                                    f"cascadă de {links} legături ({links + 1} substantive)", True))
    if counts:
        total = sum(c[0] for c in counts)
        avg = total / len(counts)
        longest = max(counts)
        stats.update(sentences=len(counts), average=round(avg, 1),
                     longest=longest[0], longest_line=longest[1])
        if avg > 20:
            findings.append(Finding("5.1", "N", 1, "(tot textul)",
                                    "fraze mai scurte",
                                    f"media este {avg:.1f} cuvinte pe frază; Mic ghid: în medie 20", False))


# ---------------------------------------------------------------------------
# D1 — consistency sets (inlocuiri.md §9). Inflected forms by pattern.
# ---------------------------------------------------------------------------

SETS = [
    ("setări", {
        "configurare": r"\bconfigur(are|area|ări|ării|ările|ărilor)\b",
        "configurație": r"\bconfigurați(e|a|ei|i|ile|ilor)\b",
        "setări": r"\bsetăr(i|ile|ilor)\b|\bsetare(a)?\b",
        "parametri": r"\bparametr(i|ii|ilor|u|ul|ului)\b",
        "opțiuni": r"\bopțiun(e|ea|i|ii|ile|ilor)\b",
    }),
    ("ștergere", {
        "a șterge": r"\bșter(ge|g|geți|gem|s|să|se|și|gerea|gere)\b",
        "a elimina": r"\belimin(a|ă|ați|at|ată|ate|ați|area|are|ării)\b",
        "a suprima": r"\bsuprim(a|ă|ați|at|ată|ate|area|are)\b",
        "a înlătura": r"\bînlătur(a|ă|ați|at|ată|ate|area|are)\b",
        "a radia": r"\bradi(a|ază|ați|at|ată|ate|erea|ere)\b",
    }),
    ("eroare", {
        "eroare": r"\beror(i|ile|ilor)\b|\beroare(a)?\b|\berorii\b",
        "problemă": r"\bproblem(ă|a|e|ele|elor|ei)\b",
        "defecțiune": r"\bdefecțiun(e|ea|i|ii|ile|ilor)\b",
        "incident": r"\bincident(ul|ului|e|ele|elor)?\b",
        "disfuncționalitate": r"\bdisfuncționalit(ate|atea|ăți|ății|ățile|ăților)\b",
    }),
    ("verificare", {
        "verificați": r"\bverific(ați|ă|a|at|ată|ate|are|area|ării|ăm)\b",
        "asigurați-vă că": r"\basigura?ți-vă\b",
        "confirmați": r"\bconfirm(ați|ă|a|at|ată|ate|are|area|ării|ăm)\b",
        "validați": r"\bvalid(ați|ează|at|ată|are|area|ării)\b",
        "controlați": r"\bcontrol(ați|ează|at|ată|are|area)\b",
    }),
    ("rulare", {
        "a rula": r"\brul(a|ează|ați|at|ată|are|area|ării)\b",
        "a executa": r"\bexecut(a|ă|ați|at|ată|ate|are|area|ării)\b",
        "a lansa": r"\blans(a|ează|ați|at|ată|are|area)\b",
        "a porni": r"\bporn(i|ește|iți|it|ită|ire|irea)\b",
    }),
    ("afișare", {
        "a afișa": r"\bafiș(a|ează|ați|at|ată|ate|are|area)\b",
        "a arăta": r"\bar(ăta|ată|ătați|ătat|ătată|ătate)\b",
        "a prezenta": r"\bprezint(ă|ăm)\b|\bprezent(ați|at|ată|ate|area|are)\b",
        "a reda": r"\bred(ă|ați|at|ată|ate|area)\b",
    }),
    ("utilizator", {
        "utilizator": r"\butilizator(ul|ului|i|ii|ilor)?\b|\butilizatoare\b",
        "client": r"\bclien(t|tul|tului|ți|ții|ților)\b",
        "beneficiar": r"\bbeneficiar(ul|ului|i|ii|ilor)?\b",
        "solicitant": r"\bsolicitan(t|tul|tului|ți|ții|ților)\b",
        "petent": r"\bpeten(t|tul|tului|ți|ții|ților)\b",
    }),
    ("cerere", {
        "cerere": r"\bcerer(e|ea|ii|i|ile|ilor)\b",
        "solicitare": r"\bsolicit(are|area|ări|ării|ările|ărilor)\b",
        "petiție": r"\bpetiți(e|a|ei|i|ile|ilor)\b",
        "sesizare": r"\bsesiz(are|area|ări|ării|ările|ărilor)\b",
    }),
    ("document", {
        "document": r"\bdocument(e|ul|ului|ele|elor)?\b",
        "act": r"\bact(e|ul|ului|ele|elor)?\b",
        "înscris": r"\bînscris(ul|ului|uri|urile|urilor)\b",
        "documentație": r"\bdocumentați(e|a|ei|i|ile|ilor)\b",
    }),
    ("termen", {
        "termen": r"\btermen(ul|ului)?\b(?!\s+limită)",
        "termen limită": r"\btermen(ul|ului)?\s+limită\b",
        "scadență": r"\bscadenț(ă|a|e|ei|ele|elor)\b",
        "dată limită": r"\bdat(a|ă)\s+limită\b",
    }),
]


def check_sets(masked, findings):
    for name, members in SETS:
        found = {}
        for label, rx in members.items():
            hits = list(re.finditer(rx, masked, re.I))
            if hits:
                found[label] = hits
        if len(found) > 1:
            first = min(h[0].start() for h in found.values())
            summary = ", ".join(f"{k} ×{len(v)}" for k, v in found.items())
            findings.append(Finding("1.5", "N", line_of(masked, first), summary,
                                    "alegeți un singur termen",
                                    f"sinonime rotite (setul „{name}”, inlocuiri.md §9) — "
                                    "verificați dacă numesc același concept", True))


# ---------------------------------------------------------------------------

def run(text):
    masked = mask(text)
    findings, stats = [], {}
    check_patterns(masked, findings)
    check_sentences(masked, findings, stats)
    check_sets(masked, findings)
    findings.sort(key=lambda f: (f.line, f.rule))
    return findings, stats


TIER_ORDER = [("N", "Normative [N] — de corectat"),
              ("S", "Stil [S] — recomandări"),
              ("F", "De semnalat [F] — decizie umană")]


def report(name, findings, stats):
    by = {t: [f for f in findings if f.tier == t] for t, _ in TIER_ORDER}
    out = [f"## Verificare — {name}", ""]
    out.append(f"**Rezumat:** {len(findings)} constatări — {len(by['N'])} normative [N], "
               f"{len(by['S'])} de stil [S], {len(by['F'])} de semnalat [F].")
    if stats:
        out.append(f"Fraza cea mai lungă: {stats['longest']} de cuvinte (linia "
                   f"{stats['longest_line']}). Media: {stats['average']} "
                   f"({stats['sentences']} fraze).")
    for tier, title in TIER_ORDER:
        if not by[tier]:
            continue
        out += ["", f"### {title}"]
        for i, f in enumerate(by[tier], 1):
            fix = f" → `{f.fix}`" if f.fix else ""
            mark = " · de verificat" if f.candidate else ""
            text = re.sub(r"\bCOD\b\s*", "[cod] ", re.sub(r"\s+", " ", f.text)).strip()
            out.append(f"{i}. Regula {f.rule} · `{text}` (linia {f.line}){fix} · {f.note}{mark}")
    out += ["", "Scriptul acoperă doar verificările mecanice. Rulați în continuare "
                "verificare.md B0.4, C, E și F (agenți, integritate, structură)."]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+", help="fișiere de verificat, sau - pentru stdin")
    ap.add_argument("--json", action="store_true", help="ieșire JSON")
    args = ap.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    any_findings, results = False, []
    for path in args.files:
        try:
            text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError) as e:
            print(f"eroare: {path}: {e}", file=sys.stderr)
            return 2
        findings, stats = run(text)
        any_findings = any_findings or bool(findings)
        if args.json:
            results.append({"file": path, "stats": stats,
                            "findings": [asdict(f) for f in findings]})
        else:
            print(report(path, findings, stats))
            print()
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if any_findings else 0


if __name__ == "__main__":
    sys.exit(main())
