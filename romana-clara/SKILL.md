---
name: romana-clara
description: |
  Write or rewrite Romanian text so it is clear, direct, and hard to misread —
  the Romanian counterpart of Simplified Technical English, built on Legea
  24/2000, the European Commission's "Mic ghid de redactare clară", DOOM 3, and
  CLEAR Global's Romanian plain-language rules. Use for any Romanian
  documentation, procedure, manual, error message, official letter, notice,
  contract, policy, internal report, or email. Also use when the user says
  "română clară", "limbaj clar", "limbaj simplu", "simplifică textul",
  "rescrie în română simplă", "scoate limbajul de lemn", "fără birocratisme",
  "de-slop", "make this Romanian readable", or asks for Romanian text that a
  tired reader, a translator, or a machine can parse on the first pass. Trigger
  this whenever you are about to produce more than a paragraph of Romanian prose
  that someone will have to act on, even if the user did not ask for
  simplification by name.
license: MIT
compatibility: claude-code cowork cursor codex gemini-cli opencode
metadata:
  version: 1.2.0
  anchors: >-
    Legea 24/2000 (republicată) Art. 8, 36, 37, 38; DOOM 3 (Academia Română,
    2021); DOOM² (2005); Legea 183/2006 + Ordin MCTI 414/2006; Mic ghid de
    redactare clară (Comisia Europeană, 2015); Ghid practic comun
    (PE/Consiliu/Comisie); CLEAR Global RO (2022); SR EN IEC/IEEE 82079-1:2020
  note: >-
    No official controlled Romanian exists. This skill assembles binding norms,
    EU guidance, and marked editorial judgment into one working rule set.
---

# Română Clară — Write Romanian That Cannot Be Misread

Romanian has no ASD-STE100. There is no approved dictionary, no maintenance group, no controlled Romanian. What Romanian *does* have is scattered across a statute, an EU booklet, an orthographic norm, and a humanitarian tipsheet — none of which talk to each other.

This skill puts them in one place and adds the missing structural discipline.

Write for a reader who is tired, in a hurry, and possibly reading Romanian as a second language — or for a machine that has to translate the text or act on it. **Each sentence must survive one read.** A sentence that needs a second pass has failed, no matter how correct it is.

**The Romanian-specific thing to understand before you start:** bureaucratic Romanian is not primarily *long*. It is *dense*. A 15-word sentence built on a five-link chain of genitives and `de` — `Prezenta procedură are ca scop stabilirea modalității de realizare a activității de verificare a documentelor` — is harder than a 24-word sentence with two finite verbs. Word limits alone will not catch it. Rules 2.10 and 2.11 exist for exactly this, and in official Romanian they do more work than every other rule combined.

## Your Task

When asked to write or rewrite Romanian text:

1. **Pick the mode** — pragmatic (default) or strict.
2. **Pick the register** — tehnic, administrativ, business, or juridic. The registers genuinely disagree about how you address the reader.
3. **Classify each passage** as procedural or descriptive. Almost every other rule depends on this.
4. **Fix your vocabulary before you draft.** Choose one verb for the verify concept (`verificați` / `asigurați-vă că` / `confirmați` — pick ONE). Choose one noun for settings (`configurare` / `setări` / `parametri` — pick ONE). Use no other word for that concept anywhere. *(Write mode only — in check mode, report the rotation you find instead.)*
5. **Apply the catalog.**
6. **Run the self-check.** It is short and it is not optional.
7. **Never touch code, identifiers, commands, legal citations, or quoted errors.** See Intangibile.

When asked to CHECK Romanian text rather than write it, report each finding as: rule number, the offending text, a compliant rewrite, and the evidence tier. Cite only rule numbers that appear in this file — do not invent them and do not import ASD-STE100 numbering, which does not apply to Romanian. For a finding that comes from a substitution table rather than a numbered rule, cite the table (`inlocuiri.md §3`) and give it a tier anyway.

## Evidence Tiers — Read This Before You Cite Anything

Every rule carries a tag. This exists because it is very easy to state a Romanian "rule" that no source actually supports, and a fabricated ruling is worse than a missing one.

| Tag | Meaning | How to present it |
|---|---|---|
| **[N]** | Normative. A statute, DOOM, or an official EU guide says this, in these words. | You may cite the source by name. |
| **[S]** | House style. Defensible and widely practiced, but no Romanian authority rules on it. | Present as a recommendation, never as "the rule says". |
| **[F]** | Flag only. Detectable but not decidable without knowing intent or context. | Raise it for a human. Never auto-fix. |

A rule can carry a quote at **[N]** and a threshold at **[S]** — the source said *20 words on average*, it did not say *25 per sentence*. Where that happens, the split is marked.

Some [S] rules are **attested**: a named source says them, but the source is not a statute, DOOM, or an official EU guide — the CLEAR Global RO tipsheet (an NGO), a linguistics paper, or an English-only or paywalled standard. Name the source when you use such a rule; do not call it a rule of Romanian.

If a user challenges a rule, tell them the tier honestly. An [S] rule is your judgment, and they are entitled to overrule it.

## Two Modes

| Mode | When | What you apply |
|---|---|---|
| **Pragmatic** (default) | Docs, letters, emails, reports — the user wants clear Romanian | All structural rules. Domain and specialist vocabulary stays (`webhook`, `endpoint`, `uzufruct`, `deviz`). |
| **Strict** | The user names Legea 24/2000, compliance, machine translation, or says "strict" | Structural rules + full vocabulary discipline + the word limits enforced hard + the neologism rule applied aggressively. Tell the user that Romanian has no certifiable plain-language standard, so "compliant" means "consistent with these named sources", not "certified". |

## Step 1: Register

The registers conflict on one real point — how you address the reader — so decide before you write, and say which you chose.

| Register | Address | Tone target | The agent of an action |
|---|---|---|---|
| **Tehnic** | Imperative: `Instalați pompa.` `dumneavoastră` is usually noise. | Neutral, operational. | The system or the user, named. |
| **Administrativ** | `dumneavoastră`, never `tu`, never bare `voi`. Imperatives for the reader's own actions are normal and correct (`Completați dosarul`). | Institutional but not defensive. An authority states what it does; it does not complain about what the law forces it to do. | Name the institution: `Direcția Fiscală analizează cererea`. |
| **Business** | `dumneavoastră` externally, `noi` / `echipa` internally. | Direct, unpadded. | Name the team. |
| **Juridic** | Third person, the parties named. | Sober, dispositive. | The party, named. |

**On the `voi` / `noi` conflict.** CLEAR Global RO recommends `voi` and `noi`. That advice was written for humanitarian messaging and does not transfer to a Romanian public authority, so the register table overrules it **on the pronoun point only**. Every other CLEAR Global rule cited in this file stands at its stated tier.

**In juridic register, precision outranks simplicity.** Where they collide, precision wins, and you say which sentence you did not touch.

## Step 2: Procedural or Descriptive

| | Procedural (instrucțiuni) | Descriptive (explicații) |
|---|---|---|
| Purpose | Tell the reader what to do | Explain what a thing is or does |
| Verb form | Imperative: `Apăsați butonul Salvare.` | Simple present, past, or future |
| Sentence ceiling | **20 words** (Rule 4.1) | **25 words** (Rule 5.1) |
| Unit rule | One instruction per sentence (4.2) | One idea per sentence, one topic per paragraph (5.2, 5.4) |

Do not mix them in one passage. A note inside a procedure is descriptive: it informs, it does not instruct, and it gets the 25-word limit (Rule 4.5).

**What the 20 actually is.** *Mic ghid de redactare clară* states `1 frază = în medie 20 de cuvinte` — an **average**, and the guide explicitly invites variation. That average is **[N]**. The per-sentence *ceilings* of 20 and 25 are this skill's operationalization of it and are **[S]**. Do not tell a user that 21 words breaks a rule; tell them the document average is what the source sets. (CLEAR Global also gives 20, but scoped `în engleză` — it does not independently confirm a Romanian figure.)

**And remember the ceilings are the weaker test.** See Rules 2.10 and 2.11.

# CATALOGUL DE REGULI

Eight sections. Cite by number.

## Secțiunea 1 — Cuvinte

| Rule | Instruction | Tier |
|---|---|---|
| 1.1 | Use everyday modern Romanian words in their current meaning. Avoid regionalisms and archaisms. — *L. 24/2000 Art. 36 alin. (4)* | **[N]** |
| 1.2 | Do not use a neologism when a widely known Romanian synonym exists. — *L. 24/2000 Art. 36 alin. (2)* | **[N]** |
| 1.3 | If a foreign term is unavoidable, give the Romanian equivalent next to it. — *L. 24/2000 Art. 36 alin. (2)* | **[N]** |
| 1.4 | Use specialist terms only when they are established in that field. Your domain vocabulary is legal: `endpoint`, `commit`, `uzufruct`, `deviz`. — *L. 24/2000 Art. 36 alin. (3)* | **[N]** |
| 1.5 | One concept, one term. Do not write `configurare` here and `setări` there. — *L. 24/2000 Art. 37 alin. (1)*; *Ghid practic comun, Orientarea 6* | **[N]** |
| 1.5a | A short form is allowed, and is not a second term: introduce it once — `serviciul de sincronizare în fundal (serviciul)` — then use the short form everywhere. Rule 1.5 forbids rotation, not abbreviation. Without this, long terms make the rewrite more repetitive than the original. | **[S]** |
| 1.6 | If a term is not established, or can be read more than one way, define it once at the start and then use it identically. — *L. 24/2000 Art. 37 alin. (2)* | **[N]** |
| 1.7 | Expand every abbreviation at first use. — *L. 24/2000 Art. 37 alin. (3)*; *Mic ghid, Rec. 9* | **[N]** |
| 1.8 | Prefer the concrete word to the abstract one when they mean the same thing: `a substitui` → `a înlocui`; `oportunități de muncă` → `locuri de muncă`. — *Mic ghid, Rec. 8* | **[N]** |
| 1.9 | Do not use words with emotional charge in normative or official text. — *L. 24/2000 Art. 8 alin. (4)* | **[N]** |
| 1.10 | Prefer the more frequent of two words that mean the same thing. Romanian readers rate rarer words as harder. But the effect is weaker in Romanian than in English, so this is judgment, not a lookup. | **[S]** |
| 1.11 | Replace corporate anglicisms that have a normal Romanian equivalent: `deadline` → `termen`, `training` → `curs`, `target` → `țintă`. Keep the anglicism when it is the established technical term (Rule 1.4). | **[S]** |

**Înainte:** Comisia a hotărât că se va demara procedura de identificare a soluțiilor optime.
**După:** Comisia a hotărât să caute cele mai bune soluții.

The agent comes from the source sentence. Without `Comisia a hotărât`, the rewrite would have to keep the impersonal form (see 2.2 vs 2.6).

## Secțiunea 2 — Verbe și densitate (the section that matters most in Romanian)

English STE fights the passive. Romanian has four ways to hide who does what and one way to make a short sentence unreadable. This is where most of your work is.

| Rule | Instruction | Tier |
|---|---|---|
| 2.1 | **Name the agent.** State who does the action. — *Mic ghid, Rec. 5*: `Indicați agenții fiecărei acțiuni` | **[N]** |
| 2.2 | **Rewrite the reflexive passive** (`se va proceda`, `se comunică`, `se efectuează`) as an active verb with a named subject — **when the agent is recoverable from the text you have.** | **[S]** |
| 2.3 | **Turn nominalizations back into verbs.** `efectuarea verificării` → `a verifica`. — *Mic ghid, Rec. 6*: `Evitați substantivele inutile – formele verbale sunt mai dinamice` | **[N]** |
| 2.4 | **Do not stack modifiers on a noun.** — attested by *CLEAR Global RO*: `Evitați șirurile de substantive`. The working ceiling of three is this skill's. | **[S]** |
| 2.5 | **Use the gerunziu only when its subject is unmistakable and adjacent.** Ambiguous attachment, doubled temporal-plus-causal reading, or distance from its controller each mean: rewrite as a finite clause. (Șuteu, *Limba română* VI/5, 1957.) | **[F]** |
| 2.6 | The canonical passive is allowed when the agent is genuinely unknown or irrelevant. *Mic ghid* Rec. 7 is explicit: `Nu este nevoie să evitați diateza pasivă cu orice preț.` | **[N]** |
| 2.7 | In normative and procedural text use the **present tense, affirmative form**. — *L. 24/2000 Art. 38 alin. (2)* | **[N]** |
| 2.8 | Avoid `urmează a fi`, `este de menționat că`, `a fi + supin` in official prose. Write `va fi`, or delete the frame and state the fact. | **[S]** |
| 2.9 | Do not build the future out of `a urma`: `urmează să se transmită` → `transmitem` / `vom transmite`. | **[S]** |
| **2.10** | **Count the density, not just the words.** More than one abstract verbal noun (`-are`, `-ere`, `-ire`, `-ție` + genitive) in one sentence is a rewrite, whatever the word count. If a passage passes 4.1/5.1 and still reads as opaque, count nouns against finite verbs: above roughly 3:1, density is the fault. | **[S]** |
| **2.11** | **Break the genitive cascade.** `stabilirea modalității de realizare a activității de verificare a documentelor` is a chain of nouns linked by `de` and by genitive articles (`a`, `al`, `ai`, `ale`). Two links is the ceiling. Adding prepositions does not fix it — they are already there. **Turn the head noun back into a finite verb and let the rest become its object:** `stabilește cum se verifică documentele`. | **[S]** |
| **2.12** | **Apply the modal ladder** (below). | mixed |

### 2.2 vs 2.6 — the tiebreaker

These two rules pull opposite ways and you will hit the conflict constantly. The test:

> Rewrite the passive **only if the agent is recoverable from the text in front of you.** If naming the agent means guessing who it is, the passive stays.

Inventing an agent breaks Intangibile and is the worse error. `datele nu se sincronizează` is a correct final answer when nothing in the source says what does the syncing.

### 2.12 — Scara modalelor

Romanian modals leak obligation. This matters double when the reader is an agent or a contractor.

| You wrote | Write instead | Tier |
|---|---|---|
| `ar trebui` | **[F] — do not swap mechanically.** Decide first: is this an obligation or a suggestion? An obligation becomes `trebuie`; a suggestion is stated as fact or deleted. Turning a recommendation into `trebuie` silently creates a duty that the drafter did not write. If you cannot tell from the document, flag it and ask. | **[F]** |
| `ar putea` / `s-ar putea` / `eventual` (possibility) | `poate` | **[S]** |
| `este posibil să` | `poate` | **[S]** |
| `poate … eventual` | Drop `eventual` — `poate` already carries the possibility. | **[S]** |
| `se recomandă` | Name who recommends, or turn it into an instruction. | **[S]** |
| `ar fi de dorit` | `trebuie`, or delete — same [F] test as `ar trebui`. | **[F]** |
| `este necesar să se efectueze` | the imperative: `efectuați` | **[S]** |

### Exemple

Every agent named in these rewrites is already in the source sentence. None is guessed.

**Reflexive passive → named agent (2.2):**
**Înainte:** Comisia de evaluare a primit cererea dumneavoastră. Se va proceda la analizarea cererii și se va comunica rezultatul.
**După:** Comisia de evaluare a primit cererea dumneavoastră. Comisia va analiza cererea și vă va comunica rezultatul.

**Nominalization → verb (2.3):**
**Înainte:** În vederea asigurării respectării termenelor, se impune efectuarea unei verificări lunare a dosarelor de către responsabilul de proiect.
**După:** Pentru a respecta termenele, responsabilul de proiect verifică dosarele în fiecare lună.

**Genitive cascade (2.11):**
**Înainte:** Prezenta procedură are ca scop stabilirea modalității de realizare a activității de verificare a documentelor.
**După:** Această procedură stabilește cum se verifică documentele.

**Gerunziu (2.5)** — in a letter the institution signs, so `noi` is the institution:
**Înainte:** Având în vedere faptul că documentul a fost depus după termen, acesta se respinge.
**După:** Întrucât documentul a fost depus după termen, îl respingem.

## Secțiunea 3 — Fraze

| Rule | Instruction | Tier |
|---|---|---|
| 3.1 | Write short, complete sentences. — *Mic ghid, Rec. 4* (short). Short does not mean elliptical — keep articles, keep `că`, keep `pe care` (**[S]**). | **[N]** / **[S]** |
| 3.2 | Put the important information at the start, not buried mid-sentence. — *Mic ghid, Rec. 5*; *CLEAR Global RO* | **[N]** |
| 3.3 | Present actions in the order they happen. — *Mic ghid, Rec. 5* | **[N]** |
| 3.4 | Use a vertical list when a sentence carries several conditions or several items. — attested by *CLEAR Global RO*. The working trigger (more than two conditions, more than three items) is this skill's. | **[S]** |
| 3.5 | Connect related sentences explicitly: `Apoi`, `Prin urmare`, `În caz contrar`, `Dacă nu`. | **[S]** |
| 3.6 | Do not stack subordinate clauses. Two levels is the practical ceiling. | **[S]** |
| 3.7 | Do not use the semicolon to join two independent statements. Write two sentences. | **[S]** |

## Secțiunea 4 — Text procedural

| Rule | Instruction | Tier |
|---|---|---|
| 4.1 | Ceiling of **20 words** per sentence, warnings included. Document average near 20 is the normative part (see Step 2). | **[S]** / avg **[N]** |
| 4.2 | One instruction per sentence, unless two actions genuinely happen at once. | **[S]** |
| 4.3 | Write instructions in the imperative: `Rulați migrarea.` `Depuneți cererea la ghișeul 3.` | **[S]** |
| 4.4 | **Condition before command**, separated by a comma: `Dacă build-ul eșuează, citiți jurnalul.` Never the reverse. | **[S]** |
| 4.5 | Notes inform, they never instruct. A note gets the 25-word limit. | **[S]** |
| 4.6 | Number the steps when order matters. Use bullets only when it does not. | **[S]** |

**Înainte:** Va trebui să obțineți cheia API din tabloul de bord înainte de a configura clientul, lucru care se poate realiza din secțiunea Setări.
**După:** Deschideți tabloul de bord, secțiunea Setări. Copiați cheia API. Apoi configurați clientul cu această cheie.

## Secțiunea 5 — Text descriptiv

| Rule | Instruction | Tier |
|---|---|---|
| 5.1 | Ceiling of **25 words** per sentence; keep the document average near 20. — *Mic ghid, Rec. 4* (the average) | **[S]** / avg **[N]** |
| 5.2 | One new fact per sentence. Build the picture gradually. | **[S]** |
| 5.3 | Use informative headings, not decorative ones. — *Mic ghid, Rec. 3* | **[N]** |
| 5.4 | One topic per paragraph; six sentences is the practical ceiling. | **[S]** |
| 5.5 | No imperative in a passage classified as descriptive. Descriptions explain; procedures instruct. | **[S]** |

## Secțiunea 6 — Avertismente și siguranță

Everything in this section is **[S]**, attested by named standards. The severity ladder comes from the ANSI Z535 / ISO 3864-2 tradition that SR EN IEC/IEEE 82079-1:2020 (adopted in Romania by ASRO) builds on. The **order** inside a warning (Rules 6.2–6.3) comes from ASD-STE100 Rule 7.2, an English-only specification. Placing the warning before the step (Rule 6.4) is attested for 82079-1 only through secondary sources, because the clause text is paywalled. None of these is a statute, DOOM, or an EU guide, so none is **[N]**. Name the standard when you apply a rule. The **Romanian labels** below are this skill's coinage — the ASRO adoption is an English-text endorsement, so no official Romanian wording exists. If your organization already uses different Romanian labels, keep yours and keep them consistent.

| Signal word | Severity (per the standard) | Tier |
|---|---|---|
| **PERICOL** (DANGER) | Imminent hazard that **will** cause death or serious injury | **[S]** |
| **AVERTISMENT** (WARNING) | Hazard that **could** cause death or serious injury | **[S]** |
| **ATENȚIE** (CAUTION) | Hazard that could cause **minor or moderate injury** | **[S]** |
| **NOTĂ** (NOTICE) | **Property, data, or equipment damage — no personal injury** | **[S]** |

Do not use ATENȚIE for data loss. Data loss is NOTĂ. Conflating the two is exactly the error the severity ladder exists to prevent.

| Rule | Instruction | Tier |
|---|---|---|
| 6.1 | Choose the signal word by severity, from the table above. — *82079-1, Clause 7* | **[S]** |
| 6.2 | Give the command or the condition **first**. — *ASD-STE100 Rule 7.2* (English) | **[S]** |
| 6.3 | Give the risk and the consequence **second**. Every warning must state what to do, what the hazard is, and what happens if the reader ignores it. | **[S]** |
| 6.4 | Place the warning **before** the step it applies to, never after. — *82079-1, Clause 7* (via secondary sources) | **[S]** |

**Înainte:** Trebuie menționat faptul că, în anumite situații, se poate produce pierderea datelor în cazul în care opțiunea de forțare este activată în mediul de producție.
**După:** NOTĂ: Nu activați opțiunea de forțare în mediul de producție. În anumite situații, opțiunea duce la pierderea datelor.

The qualifier `în anumite situații` stays (F4). The rewrite does not name the flag or explain what gets lost, because the source does neither. If the document names them elsewhere, use them.

## Secțiunea 7 — Ortografie și punctuație (mechanical, Romanian-specific)

These are the checks a machine can actually run. Several are legally grounded.

| Rule | Instruction | Tier |
|---|---|---|
| 7.1 | **Diacritics are mandatory.** DOOM 3: `Folosirea semnelor diacritice este obligatorie.` | **[N]** |
| 7.2 | **Use comma-below, not cedilla.** Correct: `ș` U+0219, `Ș` U+0218, `ț` U+021B, `Ț` U+021A. Wrong: `ş` U+015F, `ţ` U+0163 — a Windows-era encoding artifact. — *DOOM 3*; *Legea 183/2006* + *Ordin MCTI 414/2006*, whose annex lists exactly these four codepoints and no cedilla variants | **[N]** |
| 7.3 | Use `â` inside words and `î` at the edges; use the form `sunt`, not `sînt`. Keep `î` inside a word when it starts the second element of a prefixed or compound word: `neîncredere`, `reîntoarcere`, `bineînțeles`. — *Mic ghid, Rec. 10*; *DOOM 3* | **[N]** |
| 7.4 | **`pe care` is obligatory** for a relative pronoun functioning as direct object: `cartea pe care am citit-o`, not `cartea care am citit-o`. — *DOOM² (2005), p. XCIII* | **[N]** |
| 7.5 | `datorită` only for causes with a positive outcome. Otherwise `din cauza`: `din cauza prăbușirii malului`. | **[S]** |
| 7.6 | Do not insert `ca și` to dodge a cacophony. Use `ca`. Keep `ca și` in a real comparison. | **[S]** |
| 7.7 | `din punctul de vedere al X` (articulated + genitive) or `din punct de vedere X` (+ adjective). Never `din punct de vedere al X`. | **[S]** |
| 7.8 | Comma before `care`: present for an explanatory clause, absent for a defining one. Semantic distinction. | **[F]** |
| 7.9 | Cacophony: do not enforce. DOOM 3 does not rule on it, and the "accepted cacophonies" lists have no normative status. | **[F]** |
| 7.10 | Remove **true** pleonasms: `alegeri electorale` → `alegeri`; `a preciza foarte clar` → `a preciza`. See `inlocuiri.md` §7 — and note which entries there are **not** safe to auto-correct. | **[S]** |
| 7.11 | In normative text, do not explain things in parentheses. — *L. 24/2000 Art. 38 alin. (3)* | **[N]** |
| 7.12 | `etc.` and `ș.a.m.d.` → write `și altele`, which preserves the fact that the list is open. Naming the items is better **only when the source tells you what they are** — otherwise you would be inventing them (see F5). Deleting `etc.` outright loses information. | **[S]** |
| 7.13 | Check the hyphens and clitics — the commonest real Romanian error after diacritics: `s-a` (verb) vs `sa` (possessive); `într-un`, `dintr-o`, `printr-un`; `ne-am`, `v-a` vs `va`; `de-a lungul`. | **[S]** |
| 7.14 | Latin abbreviations: write `de exemplu` and `adică` in full. | **[S]** |

## Secțiunea 8 — Cum se numără cuvintele

So that limits are enforceable and two auditors get the same number:

| Rule | Instruction |
|---|---|
| 8.1 | Code spans, commands, file paths, and quoted text in backticks count as **one word**. |
| 8.2 | A number with its unit counts as one word: `30 de zile`, `12,5 %`, `5432`. A number with a unit **and a qualifier** counts as **two**: `15 zile lucrătoare`. |
| 8.3 | A legal citation counts as one word: `art. 36 alin. (2) din Legea nr. 24/2000`. |
| 8.4 | A hyphenated word counts as one word. |
| 8.5 | A proper noun or an institution name counts as one word, however many words it contains. |
| 8.6 | A cross-reference with a number counts as **two**: `anexa 1`, `ghișeul 3`. |
| 8.7 | The lead-in colon of a vertical list ends a sentence for counting. Each list item is counted on its own. |

# DISCIPLINA VOCABULARULUI

## Attested substitutions — you may cite these

From *Mic ghid de redactare clară* (European Commission, 2015). **[N]**

| Înainte | După |
|---|---|
| având în vedere faptul că | întrucât |
| în cazul în care | dacă |
| în cazul în care nu se aplică aceasta | în caz contrar |
| dacă acesta este cazul | dacă da |
| în scopul de | pentru |
| în cadrul | în |
| drept rezultat / în consecință | prin urmare |
| cu referire la | referitor la / despre |
| un anumit număr de | câteva |
| o mare parte dintre | majoritatea |
| a substitui | a înlocui |
| a demara / a debuta | a începe |
| a identifica soluții | a găsi soluții |
| oportunități de muncă | locuri de muncă |
| evoluție negativă | recesiune / regres |
| evoluție pozitivă | progres / reușită |
| prin acțiunea de distrugere | distrugând |
| necesitatea planificării amplasării | este necesar să se planifice amplasarea |
| deținătorul unei vize | cel care deține o viză |
| apariția unor noi factori | au apărut noi factori |

## House-style substitutions — mark them as your judgment

Reasonable, widely practiced, **no Romanian authority rules on them.** They follow from Rule 1.2 and Rule 1.10. Present as recommendations. **[S]**

| Înainte | După |
|---|---|
| în vederea | pentru |
| în conformitate cu prevederile | conform / potrivit |
| a proceda la efectuarea | a face |
| a implementa | a aplica / a pune în practică |
| a efectua | a face |
| a solicita | a cere |
| a deține | a avea |
| a finaliza | a termina |
| a lectura | a citi |
| a concluziona | a trage concluzia |
| a se focusa pe | a se concentra pe |
| modalitate | mod |
| problematică | problemă |
| oportunitate | ocazie |
| a viza | a privi / a se referi la |
| în ceea ce privește | pentru / despre |
| datorită faptului că | pentru că / deoarece |
| în eventualitatea în care | dacă |
| anterior / în prealabil | înainte de |
| o serie de / o multitudine de | mai multe / multe |
| la nivel de aplicație | în aplicație |

**Do not apply these in juridic register without checking.** `a deține`, `a dispune de`, and `a solicita` carry distinct legal senses that `a avea` and `a cere` do not.

## Slop românesc — delete rather than replace

These carry no fact. Do not swap them; remove them. If removing one loses information, you were not looking at slop.

`merită menționat faptul că` · `este important de reținut că` · `trebuie subliniat că` · `după cum urmează` (usually) · `pur și simplu` · `ușor` (as praise — never in `ușor inflamabil`) · `fără efort` · `în mod fluid` · `robust` · `puternic` · `cuprinzător` · `performant` · `de ultimă generație` · `extrem de rapid` · `soluție de tip` · `din punct de vedere tehnic` (usually) · `este conceput pentru a` (say what it does) · `are ca scop` (say what it does) · `permite utilizatorului să` (write `puteți`) · `funcționalitate` (write `funcție`) · `a valorifica` (write `a folosi`) · `a facilita` (write `a ajuta` / `a face posibil`) · `a aborda problema` (write `a corecta eroarea`)

**`și/sau` → write `X, Y sau ambele`.** Do not "pick one" — picking one always changes the meaning. No comma before `sau`: Romanian does not use the serial comma.

## Consistency pass

Collapse synonym rotation to one term each. Rule 1.5 is statutory, so this is not optional in official text. Rule 1.5a lets you use a short form.

- `configurare` / `configurație` / `setări` / `parametri` / `opțiuni` → pick one
- `a șterge` / `a elimina` / `a suprima` / `a înlătura` → pick one
- `eroare` / `problemă` / `defecțiune` / `incident` → pick one
- `verificați` / `asigurați-vă că` / `confirmați` / `validați` → pick one
- `utilizator` / `client` / `beneficiar` / `solicitant` → pick one
- `cerere` / `solicitare` / `petiție` → pick one

Whichever you pick, use it in headings, body, tables, buttons, and error messages alike.

# INTANGIBILE

Leave these exactly as they are, even when they break every rule above:

- Code blocks, inline code, identifiers, CLI commands, flags, file paths
- Quoted error messages and log lines
- Product names, API endpoints, configuration keys
- Legal citations and article numbers: `art. 36 alin. (2) din Legea nr. 24/2000`
- Defined legal terms in a contract — if a term is defined in the definitions clause, do not "simplify" it anywhere else
- Numbers, dates, amounts, deadlines, registration numbers
- Names of institutions in their official form

**Facts are intangible too.** Rewrite the style, never the content. When the source does not give a number, a cause, an agent, or an exact term, keep the general statement. Do not invent specifics to sound concrete — a fabricated figure is a much worse failure than a long sentence.

This constrains Rules 2.2 and 2.3 directly: de-nominalizing forces you to supply a subject that the nominal form withheld. If you do not know who it is, do not name one.

# AUTOVERIFICARE ÎNAINTE DE LIVRARE

Five checks. They take under a minute and they catch most of what goes wrong.

1. **Count** the words in your three longest sentences, and compute the document average. Over 20 (procedural) or 25 (descriptive) → split. Average well over 20 → the whole text is too dense.
2. **Count the density.** In your three densest sentences, count abstract verbal nouns (`-are`, `-ere`, `-ire`, `-ție`) and count finite verbs. More than one such noun per sentence, or a noun-to-verb ratio above about 3:1 → Rules 2.10 and 2.11. **Do this even when every sentence is under the word limit** — this is the check that catches Romanian bureaucratic prose.
3. **Search** for: `se va` · `se vor` · `având în vedere` · `în vederea` · `urmează a fi` · `ar trebui` · `efectuarea` · `realizarea` · `asigurarea` · `;`. Each hit is a probable violation of Section 2 or 3.
4. **Search** every `dacă` and `în cazul în care`. Each belongs at the START of its sentence, before the command.
5. **Search** for the terms you did NOT pick in step 4 of Your Task. Replace every hit.

Then check the diacritics: no `ş` `Ş` (U+015F, U+015E) and no `ţ` `Ţ` (U+0163, U+0162) anywhere. On a machine:

```
LC_ALL=C.UTF-8 grep -nP '[\x{015E}\x{015F}\x{0162}\x{0163}]' fisier.md
```

The `LC_ALL` prefix matters — without a UTF-8 locale, `grep -P` rejects the codepoints. (Running this over the skill's own files returns hits: those are the rule text that documents the wrong characters. Expected.)

If you can run Python, `python scripts/verifica.py fisier.md` runs the mechanical part of these checks — diacritics, hyphens, word counts by Section 8, density, genitive cascades, rotated synonyms — and prints findings in the report format of `verificare.md` §G. Hits marked `de verificat` are heuristic: confirm each one before you report it. The script does not replace checks 3–5 or the integrity check.

For a full audit, use `references/verificare.md`.

# EXEMPLU COMPLET

**Înainte (typical Romanian administrative text):**

> În vederea asigurării respectării prevederilor legale în materie, se aduce la cunoștința solicitantului faptul că, urmare a analizării documentației depuse, s-a constatat că aceasta este incompletă, motiv pentru care se va proceda la suspendarea termenului de soluționare până la momentul completării, urmând ca, în situația în care completarea nu este efectuată în termen de 30 de zile de la data comunicării prezentei, cererea să fie clasată.

One sentence, 64 words by the rules in Section 8, five hidden agents, and a four-noun genitive cascade (`vederea asigurării respectării prevederilor`).

**După (administrativ register, agent named, conditions first):**

> **Dosarul dumneavoastră este incomplet.**
>
> Am analizat documentele pe care le-ați depus.
>
> **Ce trebuie să faceți:** completați dosarul în 30 de zile de la data la care ați primit această scrisoare.
>
> Dacă nu completați dosarul în acest termen, clasăm cererea.
>
> Până când completați dosarul, termenul de soluționare este suspendat.

What changed: one 64-word sentence became a heading plus four sentences, longest 13 words; `se aduce la cunoștință` / `s-a constatat` / `se va proceda` / `nu este efectuată` / `să fie clasată` all got a named agent or an imperative; `urmare a analizării` became a verb (2.3); the consequence moved to where the reader will find it; the deadline is now the most visible thing on the page. One verb — `completați` — carries the instruction throughout, with no rotation (1.5).

The deadline starts from `data comunicării`, the day the letter reaches the reader — not the date printed on it. Writing `de la data acestei scrisori` would have moved the deadline: a changed fact in a sentence that reads better (F1 in `verificare.md`).

`În vederea asigurării respectării prevederilor legale în materie` names no provision, so it carries no fact and was deleted. If the original had cited an article, the citation would stay, on its own line as `Temei legal`.

**No fact was added or removed.** The letter still does not say where to submit the documents, because the original did not either.

# LIMITE ȘI ONESTITATE

Apply this to facts and instructions. Do not apply it to literary writing, advertising, or brand voice — it removes persuasion by design. If a user asks for "română clară" on marketing copy, say so and offer it for the documentation instead.

**There is no certifiable plain Romanian.** ISO 24495-1 (and the 2025 legal-communication Part 2) have not been adopted by ASRO, Inclusion Europe's easy-to-read standards have no Romanian edition, and no validated general-purpose Romanian readability formula exists. The one validated formula, LEMI, covers children's literature only (see `surse.md` §8). This skill is an unofficial aid assembled from named sources. When someone needs formal compliance, the only binding Romanian text is Legea 24/2000, and it binds normative acts only.

Do not claim a rule is normative unless it carries **[N]** here — and where a rule is split, do not extend the [N] to the threshold.

# REFERINȚE

- `references/inlocuiri.md` — full substitution tables: attested pairs, house style, corporate anglicisms, false friends, pleonasms (including the ones that are **not** safe to auto-correct), and the extended slop list
- `references/verificare.md` — the full audit pass with searchable patterns, for check mode and final review
- `references/domenii.md` — adaptations per domain: technical documentation, administrative correspondence, business, legal, error messages, incident reports, translation prep, agent instructions
- `references/surse.md` — every source behind an **[N]** rule, with URL, verbatim quote, and what it does *not* say
