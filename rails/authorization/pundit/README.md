# Rails Authorization with Pundit

The Cohort 2 authorization recordings do not have a safe exact Pundit repository snapshot. These focused files show the completed policy boundary used by the lessons without pretending to be the historical class application.

## Reference files

- [`task_policy.rb`](task_policy.rb) defines record-level ownership rules.
- [`tasks_controller.rb`](tasks_controller.rb) shows `authorize` and `policy_scope` at the controller boundary.
- [`task_policy_spec.rb`](task_policy_spec.rb) shows the decisions that should be tested.

These files are reconstructed reference code. Add them to a Rails API that already has authenticated users, the `pundit` gem, a `Task` model, and `Task belongs_to :user`.

Run the matching policy spec with:

```sh
bundle exec rspec spec/policies/task_policy_spec.rb
```
