require "json"
require "tmpdir"

module Identifiable
  def label
    "#{self.class.name}: #{name}"
  end
end

class Task
  include Identifiable

  attr_reader :name

  def initialize(name:, completed: false)
    raise ArgumentError, "name cannot be empty" if name.strip.empty?

    @name = name
    @completed = completed
  end

  def complete!
    @completed = true
  end

  def completed?
    @completed
  end

  def to_h
    { name: name, completed: completed? }
  end
end

class ImportantTask < Task
  def label
    "IMPORTANT — #{super}"
  end
end

class TaskStore
  def initialize(path)
    @path = path
  end

  def save(tasks)
    File.write(@path, JSON.pretty_generate(tasks.map(&:to_h)))
  end

  def load
    return [] unless File.exist?(@path)

    JSON.parse(File.read(@path), symbolize_names: true).map do |data|
      Task.new(name: data[:name], completed: data[:completed])
    end
  end
end

Dir.mktmpdir do |directory|
  path = File.join(directory, "tasks.json")
  task = ImportantTask.new(name: "Verify the API")
  task.complete!

  store = TaskStore.new(path)
  store.save([task])
  loaded = store.load

  raise "persistence failed" unless loaded.one? && loaded.first.completed?
  raise "mixins or inheritance failed" unless task.label == "IMPORTANT — ImportantTask: Verify the API"
end

puts "Ruby OOP and persistence checks passed."
