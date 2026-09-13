# Code School of Guam Learning Examples

Runnable examples, focused implementation snippets, and immutable classroom code matched to Code School of Guam lessons and recordings.

This repository is the index for current reference implementations. Exact code created during a live class may remain in its original cohort repository; those examples are linked to immutable commits so the code continues to match the recording.

## How to use an example

Each lesson includes:

- the lesson objective;
- the recording and focused timestamps when available;
- a starting code snapshot;
- the completed code snapshot;
- a comparison showing what changed;
- setup and verification instructions;
- notes distinguishing the recorded implementation from current recommendations.

Try the exercise before opening the completed snapshot. Using reference code after an attempt is encouraged: run it, trace it, compare it with your work, and explain why it behaves differently.

## Complete catalogs

- [Alumni archive catalog](CATALOG.md): all 79 published Cohort 2 archive lessons, including 72 with code or guide references and 7 explicitly marked as not needing a shared answer key.
- [Lance live-class map](LANCE.md): all 106 lessons in Lance's current curriculum, including 89 with code or guide references and 17 session, milestone, or learner-owned lessons that do not need a shared answer key.

The catalogs deliberately use exact commit and compare links for recorded classroom code. Current setup and deployment guides remain moving links so learners receive the latest instructions.

## Focused current examples

| Area | Reference |
| --- | --- |
| Ruby | [Fundamentals](ruby/fundamentals/README.md) and [object-oriented programming](ruby/oop/README.md) |
| Rails APIs | [One-to-many associations](rails/associations/one-to-many/README.md), [Pundit authorization](rails/authorization/pundit/README.md), and [background jobs](rails/background-jobs/README.md) |
| JavaScript | [Fundamentals and asynchronous JavaScript](javascript/fundamentals/README.md) |
| React | [Authentication and protected routes](react/authentication/README.md) |
| Python and FastAPI | [Python fundamentals](python-fastapi/fundamentals/README.md) |

## Repository map

```text
ruby/
rails/
javascript/
react/
python-fastapi/
ai-engineering/
templates/
```

Small, isolated examples live directly in this repository. Multi-lesson applications may remain in a dedicated repository when preserving their commit history makes the lesson easier to understand.

The generated machine-readable map is stored at [data/reference-map.json](data/reference-map.json). Rebuild and verify both catalogs with `python3 scripts/build_reference_catalog.py` and `python3 scripts/validate_reference_library.py`.

## Related resources

- [Canonical CSG resources](https://github.com/Code-School-of-Guam-Alumni/Resources)
- [CSG Learning Platform](https://learn.codeschoolofguam.com)
- [Contributing and verification](CONTRIBUTING.md)
