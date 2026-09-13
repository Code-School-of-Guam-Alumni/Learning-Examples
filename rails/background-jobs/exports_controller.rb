module Api
  module V1
    class ExportsController < ApplicationController
      def create
        ExportTasksJob.perform_later(current_user.id)
        render json: { status: "queued" }, status: :accepted
      end
    end
  end
end
