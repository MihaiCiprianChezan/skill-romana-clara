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

Pick the option that matches where you use Claude. All four install the same skill.

### A. Claude app or claude.ai: upload one file

1. Download **[romana-clara.zip](https://github.com/MihaiCiprianChezan/skill-romana-clara/releases/latest/download/romana-clara.zip)**
   from the [latest release](https://github.com/MihaiCiprianChezan/skill-romana-clara/releases/latest).
2. In Claude, open **Customize → Skills**, click **+**, then **Create skill → Upload a skill**,
   and choose the file.
3. Code execution must be on: **Settings → Capabilities** (on Team and Enterprise plans,
   an owner turns it on in **Organization settings → Plugins & skills**).

The same release also has **romana-clara.skill**, the identical package in the `.skill`
format. The Claude app recognizes it when someone shares it in a chat.

### B. Claude Code: install as a plugin (gets updates)

Run these two commands inside Claude Code:

```
/plugin marketplace add MihaiCiprianChezan/skill-romana-clara
/plugin install romana-clara@romana-clara
```

To update later, run in your terminal:

```sh
claude plugin marketplace update romana-clara
claude plugin update romana-clara@romana-clara
```

### C. Claude Code: copy the folder with git

macOS, Linux, or Git Bash:

```sh
git clone https://github.com/MihaiCiprianChezan/skill-romana-clara.git
cp -r skill-romana-clara/romana-clara ~/.claude/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/MihaiCiprianChezan/skill-romana-clara.git
Copy-Item -Recurse skill-romana-clara\romana-clara "$env:USERPROFILE\.claude\skills\"
```

For one project only, copy `romana-clara/` into `.claude/skills/` inside that project.
To update, run `git pull` in the clone and copy the folder again.

### D. Other agents (Codex, Gemini CLI, Cursor, OpenCode)

These read the same open [Agent Skills](https://agentskills.io) format. Put the
`romana-clara/` folder, from the zip or from git, in the agent's skills directory or in
`~/.agents/skills/`.

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
    └── surse.md              # every source behind an [N] rule, with quotes and URLs
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

## Releasing a new version

1. Raise `version` in both `romana-clara/SKILL.md` (under `metadata`) and
   `.claude-plugin/plugin.json`. Keep the two equal.
2. Check: `claude plugin validate .` and `python -m unittest discover tests`.
3. Build the package with Anthropic's `skill-creator` packager, which leaves out `evals/`:
   `python -m scripts.package_skill <repo>/romana-clara <repo>/dist`, run from the
   skill-creator folder. Save the result as `dist/romana-clara.skill` and a copy as
   `dist/romana-clara.zip`.
4. Create a GitHub release tagged `vX.Y.Z` and attach both files. Keep the file names
   unchanged, so the download link in option A always points to the newest release.

## License

MIT. See [LICENSE](LICENSE).
