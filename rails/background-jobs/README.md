# Rails Background Job Reference

This reconstructed example shows the boundary taught in the API namespacing and background-jobs lesson: the controller enqueues slow work, while the job performs it outside the request.

- [`exports_controller.rb`](exports_controller.rb) returns `202 Accepted` after enqueueing.
- [`export_tasks_job.rb`](export_tasks_job.rb) performs the slow operation.

The immutable classroom namespace example is [CSG Cohort 2 `namespace-background-job-api`](https://github.com/CSG-Live-July-2025/namespace-background-job-api/compare/002fcefa39e9c74994154c817b4e14c7690950a2...9cba85c17d0810db46eb95429a61cf2f92bc144a).

Use the queue adapter configured for the target application and test both enqueueing and job behavior separately.
