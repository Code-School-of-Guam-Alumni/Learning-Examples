class TasksController < ApplicationController
  def index
    render json: policy_scope(Task)
  end

  def show
    task = Task.find(params[:id])
    authorize task
    render json: task
  end

  def update
    task = Task.find(params[:id])
    authorize task

    if task.update(task_params)
      render json: task
    else
      render json: { errors: task.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def task_params
    params.require(:task).permit(:name, :description, :completed)
  end
end
