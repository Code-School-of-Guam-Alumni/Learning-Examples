# Rails API: One-to-Many Associations

## What this teaches

- Plan a one-to-many relationship before changing the database.
- Create the parent model and add the foreign key to the child table.
- Define `has_many` and `belongs_to` relationships.
- Create and update child records with the parent identifier.
- Inspect the relationship through Rails and API responses.

## Recording

- Lesson: Introduction to Associations / Adding an Association Key
- Current-class source: CSG Cohort 3 weekly session with Lance
- Focused timestamps: Mapping pending from the meeting recording
- Classification: Current classroom implementation

## Exact class code

- [Starting code](https://github.com/Code-School-of-Guam-Cohort-3/organizer_api/tree/824b9035b34a)
- [Completed code](https://github.com/Code-School-of-Guam-Cohort-3/organizer_api/tree/fe0826187beb)
- [Compare the association changes](https://github.com/Code-School-of-Guam-Cohort-3/organizer_api/compare/824b9035b34a...fe0826187beb)

Code provenance: Original Cohort 3 class code, preserved in the Organizer API repository.

The completed class change adds a `User` model, a `user_id` column on tasks, `User has_many :tasks`, and `Task belongs_to :user`. It also lets the task create and update actions accept `user_id`.

## Setup

```sh
git clone https://github.com/Code-School-of-Guam-Cohort-3/organizer_api.git
cd organizer_api
git checkout 824b9035b34a
bundle install
bin/rails db:prepare
```

After attempting the exercise, inspect the completed state:

```sh
git checkout fe0826187beb
bin/rails db:prepare
```

## Optional practice

Starting from the earlier commit, add a `Project` model where a project has many tasks and each task belongs to a project. Update task creation so it accepts a project identifier.

## Done when

- A project can have multiple tasks.
- Every task is connected to one project.
- `project.tasks` and `task.project` work in the Rails console.
- The task API accepts the relationship identifier.
- Invalid relationship data produces a clear failure instead of silently creating an orphan.

## Recorded implementation and current recommendation

The recording used `add_column :tasks, :user_id, :integer`, which accurately reflects the class session. In new Rails code, prefer a reference migration when the relationship should be enforced by the database:

```rb
add_reference :tasks, :user, null: false, foreign_key: true
```

Do not rewrite the historical snapshot. Keep it exact, then explain the stronger current approach separately.

## Common mistakes

- Adding the model relationship without adding the database column.
- Adding `user_id` but forgetting `belongs_to :user`.
- Creating existing tasks before choosing how to backfill a required parent.
- Returning deeply nested associations that recurse or expose unnecessary data.

## Version and verification

- Rails schema version in completed snapshot: `2026_09_12_051104`
- Source commits and comparison reviewed: September 13, 2026
- Clean clone, bundle installation, database preparation, and available test suite verified: September 13, 2026
- Recording timestamp verification: Pending
