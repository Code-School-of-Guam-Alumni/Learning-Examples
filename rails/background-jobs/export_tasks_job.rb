class ExportTasksJob < ApplicationJob
  queue_as :default

  def perform(user_id)
    user = User.find(user_id)
    TaskExport.create_for!(user.tasks)
  end
end
