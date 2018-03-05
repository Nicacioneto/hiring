require_relative "transfer"
require "test/unit"

class TestTransaction < Test::Unit::TestCase

  $api_key ="5d81-dedd-3eb9-552d"
  $pin ="iamhopesandman"

  def test_transaction_error
    transfer = Transfer.new("2NGAyhPa8EqoE6uFU9UurkDgxmzdr9AJJC7","mnYoahiweETgdXsfY92GCWA6HoRj9knQUw")
    assert_equal(transfer.transfer, "Cannot withdraw funds without Network Fee of 0.00000000 BTCTEST. Maximum withdrawable balance is 0.00000000 BTCTEST.")
  end

end
