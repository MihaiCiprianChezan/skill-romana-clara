# Pasul de verificare — full audit pass

Use this in check mode, and for a final review of anything important. The five-check
self-check in SKILL.md catches most problems in a minute; this catches the rest.

Report findings as: **rule number · offending text · compliant rewrite · tier**.

---

## A. Mechanical checks (run these first — they are deterministic)

These need no judgment. Run them literally.

| # | Search for | Why | Rule |
|---|---|---|---|
| A1 | `ş` U+015F, `ţ` U+0163, `Ş` U+015E, `Ţ` U+0162 | Cedilla instead of comma-below. Encoding artifact. | 7.2 [N] |
| A2 | Missing diacritics. Grep only the **unambiguous** forms — `fara`, `insa`, `desi`, `daca`, `dupa`, `catre`, `astazi`, `stiu`, `acestia` (`acesta` is fine). **Do not grep `si`, `sa`, `tara`, `sant`, `tine`, `pana`** — each is also a correct Romanian word (`sa` = possessive, `tara` = defect, `tine` = pronoun, `pana` = definite form of `pană`, `si` = musical note), so they generate noise. If the document has no `ă`, `â`, `î`, `ș`, `ț` and no cedilla forms anywhere, the whole text is undiacriticized and you can say so in one line instead of listing hits. | 7.1 [N] |
| A3 | `sînt`, `cînd`, `rîu`, `mîine` | Pre-1993 î-spelling. | 7.3 [N] |
| A4 | `;` | Split into two sentences. | 3.7 [S] |
| A5 | `etc.`, `ș.a.m.d.` | Write `și altele`. Name the items only if the source says what they are. | 7.12 [S] |
| A5b | `i.e.`, `e.g.`, `cf.`, `viz.` | Write `adică`, `de exemplu`, `compară`, `vezi` in full. | 7.14 [S] |
| A6 | `și/sau` | Write `X, Y sau ambele`. Never pick one — that changes the meaning. | slop |
| A7 | `din punct de vedere al` / `din punct de vedere a` | Should be `din punctul de vedere al`. | 7.7 [S] |
| A8 | `ca și` followed by a word starting with `c` (`ca și coordonator`) | Anti-cacophony insertion. Use `ca`. Keep `ca și` in a real comparison (`la fel ca și anul trecut`). | 7.6 [S] |
| A9 | `datorită` followed by a negative noun (`pierderii`, `prăbușirii`, `eșecului`, `întârzierii`, `defecțiunii`) | Should be `din cauza`. | 7.5 [S] |
| A10 | Relative `care` immediately followed within the clause by `-o`, `l-`, `i-`, `le-`, `îl`, `o` | Missing obligatory `pe care`. | 7.4 [N] |
| A11 | `sa` where a verb is required (`sa facut`, `sa constatat`) | Should be `s-a`. | 7.13 [S] |
| A12 | `intr-un`, `dintr`, `printr` without the hyphen or with the wrong one; `va` where `v-a` is required | Clitic/hyphen errors. | 7.13 [S] |
| A13 | `de-a lungul`, `de-a latul` written without the hyphen | Same. | 7.13 [S] |

Regex for A1, if you have a shell:

```
LC_ALL=C.UTF-8 grep -nP '[\x{015E}\x{015F}\x{0162}\x{0163}]' fisier.md
```

Without a UTF-8 locale, `grep -P` refuses these codepoints with
`character code point value in \x{} is too large`. The `LC_ALL` prefix fixes it.

---

## B0. Density check — run this BEFORE counting words

This is the check that catches Romanian bureaucratic prose, and the one most likely to be
skipped. A text can pass every word limit and still be unreadable.

| # | Check | Rule |
|---|---|---|
| B0.1 | In each sentence, count abstract verbal nouns: endings `-are`, `-area`, `-ării`, `-ere`, `-erea`, `-erii`, `-ire`, `-irea`, `-irii`, `-ție`, `-ția`, `-ției`. **More than one per sentence → rewrite**, whatever the word count. The endings are a heuristic: count only nouns derived from a verb (`verificare` ← `a verifica`, `transmiterii` ← `a transmite`). `care`, `mare`, `pare`, `tare` are not nouns of this kind; `funcție`, `poziție`, `Direcția` are ordinary nouns. | 2.10 [S] |
| B0.2 | Count nouns against finite verbs across the passage. Above roughly **3:1**, density is the fault, not length. | 2.10 [S] |
| B0.3 | Find genitive cascades: a noun followed by `de` + noun, or by a genitive article (`a`, `al`, `ai`, `ale`) + noun, **more than twice in a row**. Fix by turning the head noun into a finite verb — not by adding prepositions. | 2.11 [S] |
| B0.4 | Count the sentences that have a human or institutional subject. If fewer than half do, the document has an agent problem that no per-sentence rule will surface. | 2.1 [N] |

**Worked case.** `Prezenta procedură are ca scop stabilirea modalității de realizare a
activității de verificare a documentelor.` — 15 words, under every ceiling. B0.1 finds
`stabilirea`, `realizare`, `verificare` (three). B0.3 finds a five-link cascade. B0.4 finds
no real agent. Three separate density faults in a sentence that passes B1.

---

## B. Sentence-level checks

| # | Check | Rule |
|---|---|---|
| B1 | Count words in every sentence. Procedural over 20, descriptive over 25 → split. **The ceilings are [S]** — this skill's operationalization. | 4.1, 5.1 [S] |
| B2 | Compute the document **average**. This is the normative figure: *Mic ghid* gives `1 frază = în medie 20 de cuvinte`. Average well over 20 → rewrite, even if no single sentence breaks a ceiling. | 5.1 [N] |
| B3 | Every `dacă` / `în cazul în care` / `când` / `atunci când` sits at the START of its sentence, before the command. | 4.4 [S] |
| B4 | No sentence contains two imperatives joined by `și` unless the two actions genuinely happen at the same moment. | 4.2 [S] |
| B5 | No more than two levels of subordination. Count `care`, `că`, `să`, `deoarece`, `întrucât` in one sentence — three or more is a rewrite. | 3.6 [S] |
| B6 | Paragraphs: one topic, six sentences maximum. | 5.4 [S] |
| B7 | No imperative in a passage classified as descriptive; no explanation embedded in a numbered step. | 5.5, 4.5 [S] |

**How to count** — see SKILL.md Section 8. Code spans, numbers with units, legal
citations, hyphenated words, and institution names each count as one word.

---

## C. Verb and agent checks — the highest-yield section for Romanian

| # | Search for | Then ask | Rule |
|---|---|---|---|
| C1 | `se va`, `se vor`, `se face`, `se efectuează`, `se comunică`, `se constată`, `se aduce la cunoștință`, `se impune` | Who does this? If you know, name them and use an active verb. If you genuinely do not know, the reflexive passive can stay. | 2.2 [S] |
| C2 | `a fost`, `au fost`, `este + participiu` | Same question. *Mic ghid* Rec. 7 permits the passive when the agent is unknown or irrelevant — do not de-passivize mechanically. | 2.6 [N] |
| C3 | Abstract verbal nouns. Match **all** of these, not just the definite forms: `-are`/`-area`/`-ării`, `-ere`/`-erea`/`-erii`, `-ire`/`-irea`/`-irii`, `-ție`/`-ția`/`-ției`. A list that only covers `-area` misses `realizare`, `verificare`, `transmiterii`, `întârzierii` — often half the nominalizations in the text. Note the diacritic: `-ția`, not `-atia`, or the pattern can never match correctly spelled Romanian. | 2.3 [N] |
| C4 | `având în vedere`, `urmând`, `fiind`, `luând în considerare`, and any `-ând` / `-ind` form | Is its subject unmistakable and adjacent? If not, rewrite as a finite clause. | 2.5 [F] |
| C5 | `urmează a fi`, `urmează să se`, `este de menționat`, `a fi + supin` | Write the plain future or the plain statement. | 2.8, 2.9 [S] |
| C6 | `ar putea`, `s-ar putea`, `eventual`, `este posibil să`, `se recomandă` | Apply the modal ladder, **Rule 2.12**. | 2.12 [S] |
| C6b | `ar trebui`, `ar fi de dorit` | **Do not swap mechanically.** Obligation or suggestion? `trebuie` creates a duty; if the drafter meant a recommendation you have just invented an obligation. If the document does not settle it, report it as [F] and ask. | 2.12 [F] |
| C7 | Stacked modifiers on one noun (`servicii medicale cruciale salvatoare de viață`) | Split into a short noun plus a relative clause: `servicii medicale care salvează vieți`. Adding prepositions is **not** the fix for a genitive cascade — see B0.3 and Rule 2.11. | 2.4 [N]/[S] |
| C8 | Normative or procedural text in past or conditional | Present tense, affirmative form. | 2.7 [N] |

---

## D. Vocabulary checks

| # | Check | Rule |
|---|---|---|
| D1 | Build the list of terms you rotated. Every synonym set in `inlocuiri.md` §9 that appears with more than one member is a violation. | 1.5 [N] |
| D2 | Every abbreviation expanded at first use. | 1.7 [N] |
| D3 | Every neologism: does a widely known Romanian synonym exist? If yes, and the neologism is not the established term in this field, replace it. | 1.2, 1.4 [N] |
| D4 | Every foreign term kept: is the Romanian equivalent given next to it? | 1.3 [N] |
| D5 | Run the slop list from `inlocuiri.md` §8. Delete rather than replace. | slop |
| D6 | Run the pleonasm list from `inlocuiri.md` §7. | 7.10 [S] |
| D7 | Emotional or evaluative words in official text (`din păcate`, `regretabil`, `evident`, `desigur`, `firește`). | 1.9 [N] |
| D8 | Corporate anglicisms with a normal Romanian equivalent. | 1.11 [S] |

---

## E. Structure and safety

| # | Check | Rule |
|---|---|---|
| E1 | Does the most important information come first — in the document, in the section, and in the sentence? | 3.2 [N] |
| E2 | Are the headings informative rather than decorative? `Cum depuneți cererea` beats `Aspecte procedurale`. | 5.3 [N] |
| E3 | Any sentence with more than two conditions or three items → vertical list. | 3.4 [N] |
| E4 | Every warning: signal word present (`PERICOL` / `AVERTISMENT` / `ATENȚIE` / `NOTĂ`), chosen by severity, command first, consequence second, positioned BEFORE the step. | 6.1, 6.4 [N]; 6.2–6.3 [S] |
| E5 | Are deadlines, amounts, and consequences visible without reading a full paragraph? | 3.2 [N] |
| E6 | In normative text: no explanations in parentheses. | 7.11 [N] |

---

## F. Integrity check — do this last, and do not skip it

The failure mode that matters most is not a long sentence. It is a rewrite that quietly
changed what the text says.

| # | Check |
|---|---|
| F1 | Every number, date, amount, deadline, and percentage is identical to the source. |
| F2 | Every legal citation is untouched, in its original form. |
| F3 | Every defined contractual term appears exactly as defined — not "simplified" in the body. |
| F4 | No qualifier was dropped that changes an obligation: `de regulă`, `cu excepția`, `numai dacă`, `sub condiția`, `în măsura în care`. |
| F5 | Nothing concrete was invented. If the source said "în scurt timp", the rewrite does not say "în 5 zile". |
| F6 | The set of facts in the output equals the set of facts in the input. Nothing added, nothing lost. |

If F4 or F5 fails, the rewrite is worse than the original, however readable it reads.
Stop and redo it.

---

## G. Reporting format

When you report an audit, use this shape. It is scannable and it lets the user
overrule an [S] finding without arguing about the [N] ones.

```
## Verificare — [document name]

**Rezumat:** N constatări — X normative [N], Y de stil [S], Z de semnalat [F].
Fraza cea mai lungă: NN de cuvinte. Media: NN.

### Normative [N] — de corectat
1. Regula 7.2 · `configuraţie` (linia 14) → `configurație` · cedilă în loc de virgulă
2. ...

### Stil [S] — recomandări
1. Regula 2.2 · `se va proceda la analizarea cererii` (linia 8)
   → `Comisia analizează cererea`
2. ...

### De semnalat [F] — decizie umană
1. Regula 7.8 · virgulă înainte de `care` (linia 22) — atributivă explicativă
   sau determinativă? Sensul se schimbă.
```

**Findings that have no rule number.** Some faults come from the substitution tables
(`inlocuiri.md §3`, `§8` slop) rather than the numbered catalog, and some — a missing
complement, an unrecoverable referent — have no entry at all. Cite the table, or write
`fără număr de regulă` and describe the fault. Give it a tier regardless. Never invent a
rule number to make the report look uniform.

Give the tier on every line. A user who knows which findings are binding and which are
your taste will trust the binding ones more.
