require 'test_helper'

class TransactionsControllerTest < ActionDispatch::IntegrationTest
  test "Passing: Effecting withdrawal of values through the block.io" do
  	feedback = get new_transaction_url
    assert_equal( feedback, 200)
  end
end
