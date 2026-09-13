from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    name: str
    completed: bool = False

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name cannot be empty")


def summarize_tasks(tasks: list[Task]) -> dict[str, object]:
    completed = [task for task in tasks if task.completed]
    return {
        "total": len(tasks),
        "completed": len(completed),
        "remaining": len(tasks) - len(completed),
        "names": [task.name for task in completed],
    }


tasks = [
    Task(name="Plan the schema", completed=True),
    Task(name="Build the endpoint"),
]
summary = summarize_tasks(tasks)

assert summary == {
    "total": 2,
    "completed": 1,
    "remaining": 1,
    "names": ["Plan the schema"],
}

print("Python fundamentals checks passed.")
