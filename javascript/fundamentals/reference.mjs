import assert from "node:assert/strict";

export function summarizeTasks(tasks) {
  const completed = tasks.filter((task) => task.completed);
  return {
    total: tasks.length,
    completed: completed.length,
    remaining: tasks.length - completed.length,
    names: completed.map((task) => task.name),
  };
}

export async function loadTasks(fetchTasks) {
  const tasks = await fetchTasks();
  if (!Array.isArray(tasks)) {
    throw new TypeError("Expected an array of tasks");
  }
  return tasks;
}

const tasks = [
  { id: 1, name: "Plan the schema", completed: true },
  { id: 2, name: "Build the endpoint", completed: false },
];

assert.deepEqual(summarizeTasks(tasks), {
  total: 2,
  completed: 1,
  remaining: 1,
  names: ["Plan the schema"],
});

const loadedTasks = await loadTasks(async () => tasks);
assert.equal(loadedTasks[0].id, 1);

console.log("JavaScript fundamentals and async checks passed.");
