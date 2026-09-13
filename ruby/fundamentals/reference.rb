def completed_tasks(tasks)
  tasks.select { |task| task[:completed] }
end

def task_names(tasks)
  tasks.map { |task| task[:name] }
end

def completion_summary(tasks)
  completed = completed_tasks(tasks)
  {
    total: tasks.length,
    completed: completed.length,
    remaining: tasks.length - completed.length,
    names: task_names(completed)
  }
end

tasks = [
  { name: "Plan the schema", completed: true },
  { name: "Build the endpoint", completed: true },
  { name: "Test the sad path", completed: false }
]

summary = completion_summary(tasks)

raise "wrong total" unless summary[:total] == 3
raise "wrong completed count" unless summary[:completed] == 2
raise "wrong remaining count" unless summary[:remaining] == 1
raise "wrong completed names" unless summary[:names] == ["Plan the schema", "Build the endpoint"]

puts "Completed #{summary[:completed]} of #{summary[:total]} tasks."
puts "Ruby fundamentals checks passed."
