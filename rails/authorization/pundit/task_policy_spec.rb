RSpec.describe TaskPolicy do
  subject(:policy) { described_class.new(current_user, task) }

  let(:current_user) { User.new(id: 1) }

  context "when the user owns the task" do
    let(:task) { Task.new(user_id: 1) }

    it { is_expected.to permit_actions(%i[show update destroy]) }
  end

  context "when another user owns the task" do
    let(:task) { Task.new(user_id: 2) }

    it { is_expected.to forbid_actions(%i[show update destroy]) }
  end
end
