# Contributing and Verification

## Required lesson metadata

Every example must identify:

- lesson and module;
- recording URL and focused timestamps, or `Recording mapping pending`;
- supported language and framework versions;
- starting and completed code;
- setup and verification commands;
- expected behavior;
- common mistakes;
- whether the code is original or reconstructed;
- last verification date.

## Snapshot rules

Use immutable commit links or tags for code tied to a recording. Do not link only to a moving `main` branch.

For an evolving application, prefer:

```text
lesson/<lesson-slug>/start
lesson/<lesson-slug>/complete
```

If the exact class repository already exists, link to its original commits rather than copying and silently changing the code. Add a separate current-recommendation note when the recorded implementation should be improved.

## Verification

Before marking an example verified:

1. Clone the source into a clean temporary directory.
2. Check out the starting snapshot and follow its setup instructions.
3. Check out the completed snapshot and run the documented verification.
4. Compare the completed behavior with the recording.
5. Test every link.
6. Confirm that no secret, student data, or local environment file is present.
7. Record the verification date.

Use `templates/LESSON_EXAMPLE_TEMPLATE.md` for new entries.
