# MIT Application Guide

How this repository is organised to support a strong graduate-school
(MIT / Purdue) application — and how to keep strengthening it.

## What strong applicants' repos show

1. **Real engineering** — a package that installs, has tests, and runs.
2. **Reproducible science** — pinned environments, seeded randomness, numbered notebooks.
3. **Clear communication** — a README that explains the *why*, not just the *what*.
4. **Depth over breadth** — one project taken to completion beats five half-finished ones.
5. **Ethics & care** — privacy-first handling of health data.

## How this repo delivers that

| Signal | Where |
| ------ | ----- |
| Installable package | `src/hidms/` + `pyproject.toml` |
| Tests | `tests/` (`make test`) |
| Reproducible env | `environment.yml` + `requirements.txt` |
| Research depth | `docs/thesis_outline.md` + `research` branch (Zotero library) |
| Communication | `README.md`, `docs/architecture.md` |
| Ethics | `data/README.md` privacy policy, risk-support framing |

## Checklist before you apply

- [ ] Complete Chapter 3–5 of the thesis outline with real experiments
- [ ] Commit at least one trained model + evaluation notebook with results
- [ ] Add a `CITATION.cff` and project badges
- [ ] Keep commit history clean and descriptive
- [ ] Link the repo from your CV, LinkedIn, and statement of purpose
- [ ] Write a short "Research Statement" in `docs/` summarising RQ1–RQ3 results
- [ ] (Optional) Add CI (GitHub Actions: lint + test on every push)

## Remember

A strong repo supports, but never replaces, strong grades, research letters,
and a clear statement of purpose. The repo is your **evidence of execution**.
