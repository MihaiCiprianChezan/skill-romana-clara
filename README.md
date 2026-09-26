# skill-romana-clara

An [Agent Skill](https://agentskills.io) that writes or rewrites Romanian text so it is
clear, direct, and hard to misread. It is the Romanian counterpart of Simplified Technical
English, built on Legea 24/2000, the European Commission's *Mic ghid de redactare clară*,
DOOM 3, and CLEAR Global's Romanian plain-language rules.

There is no official controlled Romanian. This skill puts the binding norms, the EU
guidance, and clearly marked editorial judgment into one rule set. Every rule carries an
evidence tier:

| Tier | Meaning |
|---|---|
| **[N]** | Normative: a statute, DOOM, or an official EU guide says it |
| **[S]** | House style: defensible, but no Romanian authority rules on it (some are attested by a named non-authority source) |
| **[F]** | Flag only: needs a human decision, never auto-fixed |

## Install

**Claude Code** (personal):

```sh
git clone https://github.com/MihaiCiprianChezan/skill-romana-clara.git
cp -r skill-romana-clara/romana-clara ~/.claude/skills/
```

For a single project, copy `romana-clara/` into `.claude/skills/` in that repository.
Other agents that read the Agent Skills format (Codex, Gemini CLI, Cursor, OpenCode) use
the same folder. Put it in their skills directory, or in `~/.agents/skills/`.

## Use

The skill triggers on Romanian documentation, letters, procedures, error messages,
contracts, and similar text, or when you ask for "română clară", "limbaj clar",
"simplifică textul", "fără birocratisme". Two modes:

- **Write/rewrite**: produces the text and says which register it used (tehnic,
  administrativ, business, juridic).
- **Check**: reports each finding as rule number · offending text · rewrite · tier.

## Contents

```
romana-clara/
├── SKILL.md                  # rules catalog, modes, registers, self-check
└── references/
    ├── inlocuiri.md          # substitution tables, pleonasms, slop list
    ├── verificare.md         # full audit pass with searchable patterns
    ├── domenii.md            # per-domain adaptations (docs, letters, legal, UI…)
    ├── surse.md              # every source behind an [N] rule, with quotes and URLs
├── scripts/
│   └── verifica.py           # mechanical checks (stdlib Python 3.8+)
└── evals/
    ├── evals.json            # behavior tests in skill-creator format
    └── trigger_eval.json     # 10 should-trigger, 10 near-miss queries
```

Run the checker on a Romanian text:

```sh
python romana-clara/scripts/verifica.py document.md
python romana-clara/scripts/verifica.py --json document.md
```

It exits 1 when it finds something. Tests: `python -m unittest discover tests`.

The evals in `romana-clara/evals/` test the model, not the script. Each case targets a
known failure: an invented agent, a moved deadline, invented numbers or commands, a
dropped qualifier. Run them with Anthropic's `skill-creator` skill, on each model you
plan to use.

## License

MIT. See [LICENSE](LICENSE).
