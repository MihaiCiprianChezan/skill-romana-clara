# Adaptări pe domenii

The catalog in SKILL.md is general. This file says how it lands in each kind of text.
Read the section you need; do not read all of them.

**Contents:** 1. Documentație tehnică · 2. Corespondență administrativă ·
3. Comunicare de business · 4. Text juridic · 5. Mesaje de eroare și interfețe ·
6. Rapoarte de incident · 7. Pregătire pentru traducere · 8. Instrucțiuni pentru agenți

---

## 1. Documentație tehnică

Register: **tehnic**. Mostly procedural.

- Imperative throughout: `Instalați`, `Rulați`, `Deschideți`, `Copiați`.
- `dumneavoastră` is noise here. Drop it.
- One instruction per numbered step. If a step has an "and", it is probably two steps.
- Condition before command, every time: `Dacă serviciul nu pornește, verificați jurnalul.`
- The command itself in backticks, untouched, counted as one word.
- A note is not a step. Put it in its own block, in descriptive form.
- Warnings come BEFORE the destructive step. Pick the signal word by severity (SKILL.md §6):
  `NOTĂ` for data or equipment damage, `ATENȚIE` for minor or moderate injury,
  `AVERTISMENT` for a hazard that **could** cause death or serious injury, `PERICOL` for one
  that **will**. Data loss is **NOTĂ**, not ATENȚIE.
- Keep `webhook`, `endpoint`, `commit`, `deploy`, `cache` — Rule 1.4 protects established
  technical terms. Do not manufacture Romanian calques nobody uses.
- But do translate the ones that have real Romanian equivalents in use:
  `a descărca` not `a downloada`, `implicit` not `by default`, `actualizare` not `update`.

**Înainte:** Utilizatorul va trebui să se asigure că serviciul rulează, lucru care poate
fi verificat prin rularea comenzii de status, înainte de a proceda la aplicarea migrării.

**După:**
1. Rulați comanda de status ca să vedeți dacă serviciul rulează.
2. Dacă serviciul rulează, aplicați migrarea.

The source does not name the command, so the rewrite does not either. If the real command
appears elsewhere in the document, put it in backticks in step 1. Do not supply a plausible
one — `systemctl status …` would be an invented fact.

---

## 2. Corespondență administrativă

Register: **administrativ**. This is where Romanian is worst and where the gain is largest.

- `dumneavoastră`, never `tu`, never bare `voi`. Romanian administrative deference is a
  real convention; CLEAR Global's "folosiți «voi» și «noi»" was written for humanitarian
  messaging and does not transfer here.
- **But deference is not the same as hiding the agent.** Name the institution:
  `Direcția Fiscală a analizat cererea`, not `s-a procedat la analizarea cererii`.
- Put the decision first. The reader wants to know the outcome, not the procedure.
- Put the deadline and the consequence where the eye lands: a bold line, or a numbered step.
- One sentence per obligation.
- Keep the legal citations exactly as they are, but move them out of the main sentence:
  give the decision in plain Romanian, then cite the basis on its own line.

**Standard shape — when the reader must act:**

```
[Ce am hotărât — o propoziție, la început]

[De ce, pe scurt]

Ce trebuie să faceți:
1. [acțiune] — până la [dată]
2. [acțiune] — până la [dată]

Ce se întâmplă dacă nu faceți acest lucru: [consecința]

Temei legal: [citare exactă]
Dacă aveți întrebări: [contact]
```

**Standard shape — when the reader need do nothing.** This is the commoner letter, and
forcing it into the template above produces an empty `Ce trebuie să faceți` section:

```
[Ce facem noi — o propoziție, la început]

[Când, cu termenul exact]

[Ce se întâmplă dacă nu putem respecta termenul]

Temei legal: [citare exactă]
Dacă aveți întrebări: [contact]
```

Do not manufacture an action for the reader in order to fill a template. If the letter is
an acknowledgement, say so and stop.

Turning `se aduce la cunoștință` into `vă informăm` is the single highest-yield edit in
Romanian administrative writing. Do it first.

---

## 3. Comunicare de business

Register: **business**. Usually descriptive with a procedural tail.

- `dumneavoastră` externally, `noi` / `echipa` internally.
- The enemy here is the anglicism, not the archaism. Run `inlocuiri.md` §5.
- Delete the empty praise (`robust`, `de ultimă generație`, `scalabil`). It is the fastest
  way to make a Romanian business document sound like it was written by a person.
- State the ask in the first two sentences. An email whose request is in paragraph four
  will not get the request done.
- Numbers beat adjectives: `am redus timpul de răspuns de la 4 zile la 1 zi`, not
  `am îmbunătățit semnificativ timpul de răspuns`.
- Subject lines are procedural: `Aprobare necesară până vineri — buget Q4`.

---

## 4. Text juridic

Register: **juridic**. Precision outranks simplicity. When they collide, precision wins.

Binding rules from Legea 24/2000 (normative acts):

- **Art. 8 alin. (4)** — clear, fluent, intelligible; no syntactic difficulty, no obscure
  or equivocal passages; no emotionally charged terms.
- **Art. 36 alin. (1)** — concise, sober, clear, precise, excluding any ambiguity.
- **Art. 36 alin. (2)** — no neologism where a widely known Romanian synonym exists.
- **Art. 36 alin. (3)** — specialist terms only when established in the field.
- **Art. 36 alin. (4)** — current modern Romanian, no regionalisms.
- **Art. 37 alin. (1)** — the same notion is expressed only by the same term.
- **Art. 37 alin. (2)** — define an unsettled term once, in the general provisions or an annex.
- **Art. 37 alin. (3)** — abbreviations expanded at first use.
- **Art. 38 alin. (1)** — dispositive text: state the norm without explanation or justification.
- **Art. 38 alin. (2)** — present tense, affirmative form.
- **Art. 38 alin. (3)** — no explanations in parentheses.

For contracts, which the law does not bind:

- Never touch a term defined in the definitions clause. Not once, anywhere.
- Never drop a qualifier: `de regulă`, `cu excepția`, `numai dacă`, `sub condiția`,
  `în măsura în care`, `fără a aduce atingere`. Each one changes the obligation.
- Split long clauses at the semicolons and the enumerations, not at the qualifiers.
- One obligation per numbered sub-clause.
- If simplification would change the legal effect, stop and tell the user which sentence
  you did not touch and why. That is a better outcome than a readable clause that means
  something else.

For translations of EU legislation, the IER *Ghid stilistic* (2008) governs, and it
pulls against this skill in three places:

- A translation keeps the number of paragraphs, sentences, and independent structures of
  the original (IER §3.5, point 15). Do not split sentences in the translated act.
- Recitals written in the `întrucât` form are separated by semicolons (IER §2.2.1.2).
  Rule 3.7 does not apply to them.
- The guide keeps `și/sau` where the source has *and/or*. Keep it.

Write in plain Romanian only around the act — summaries, cover letters, explanations —
never inside the translated text. Two IER conventions do apply to your own legal
Romanian: binding provisions in the present tense, not the future (IER §3.3.3, as Rule
2.7), and `este`, not `e`.

---

## 5. Mesaje de eroare și interfețe

Three parts, in this order: what happened · why, if known · what to do.

- What happened: simple past or simple present. `Salvarea a eșuat.`
- Why: one clause, only if you actually know. `Fișierul este blocat de alt proces.`
- What to do: imperative. `Închideți celălalt program și încercați din nou.`
- No `Ups!`, no `Ne pare rău`, no apology padding, no exclamation marks.
- Never `Vă rugăm să vă asigurați că` — write `Verificați că`, or better, name the fix.
- Buttons are verbs: `Salvați`, `Ștergeți`, `Trimiteți` — and the same verb as in the docs.
- Empty states say what to do, not that something is empty.

**Înainte:** Ups! Ceva nu a mers bine. Vă rugăm să vă asigurați că datele introduse sunt
corecte și să încercați din nou.

**După:** Data nașterii nu este validă. Folosiți formatul ZZ.LL.AAAA — de exemplu 05.03.1990.

The rewrite needs two facts the original hid: which field failed, and which format it
accepts. They come from the validation code or from the developer. If you do not have them,
ask. Without them, the honest rewrite is only `Datele introduse nu sunt valide. Verificați-le
și încercați din nou.`

---

## 6. Rapoarte de incident

Simple past. Named agents. Numbers instead of adjectives.

**Înainte:** Am identificat o problemă care este posibil să fi afectat un număr de
utilizatori și am luat măsuri pentru remedierea situației.

**După:** Între 14:02 și 14:31, 12 % dintre cereri au eșuat. Cauza a fost o configurare
greșită a bazei de date. Echipa a corectat configurarea la 14:31.

The times, the percentage, and the cause come from the incident timeline, not from the
original sentence. If you do not have the timeline, ask for it. Never fill the slots with
plausible numbers.

Structure: ce s-a întâmplat · când (interval exact) · pe cine a afectat (cifră) ·
de ce · ce am făcut · ce facem ca să nu se repete. No hedging, no `este posibil să fi` —
unless the impact is genuinely still unknown, in which case say what is unknown and when
you will know.

---

## 7. Pregătire pentru traducere și traducere automată

This is where the discipline pays for itself, and it is the original reason controlled
languages exist.

- One term, one meaning, throughout. Rotation destroys translation memory matches.
- Keep `că`, `să`, `pe care`, and every article. Elliptical Romanian mistranslates.
- Short sentences with explicit subjects. A gerunziu with an unclear subject will be
  attached wrongly by any engine.
- Avoid the reflexive `se`, which is ambiguous between passive, reflexive, and
  impersonal — engines pick wrong.
- Avoid pronouns whose referent is more than one sentence away.
- Expand abbreviations. `art.`, `alin.`, `lit.` are fine in legal text; `ș.a.` is not.
- Budget for expansion: Romanian runs longer than English. The measured figure and its
  caveats are in `surse.md` §7 — do not restate it as a standard, because it is not one.

---

## 8. Instrucțiuni pentru agenți și prompturi în română

A system prompt is a procedure written for a reader who cannot ask a follow-up question.
Everything in Section 4 of the catalog applies, plus:

- Models tend to treat `ar trebui` as optional. If it is an obligation, write `trebuie`.
  If it is a preference, say so explicitly or delete it.
- One instruction per sentence. A sentence with two instructions gets one of them followed.
- Condition first, always: `Dacă fișierul lipsește, oprește-te și întreabă.`
- Name the actor. `Se verifică` gives the model nobody to be.
- State the negative case explicitly. `Dacă nu găsești fișierul, nu inventa conținutul —
  raportează că lipsește.`
- Define every term once and never rotate it. A model that sees `configurare` and
  `setări` will assume they are two different things.
