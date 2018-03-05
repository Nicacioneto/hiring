require_relative "transfer"
require "test/unit"

class TestTransaction < Test::Unit::TestCase

  $api_key ="5d81-dedd-3eb9-552d"
  $pin ="iamhopesandman"

  def test_transfer_success
    transfer = Transfer.new("2NGAyhPa8EqoE6uFU9UurkDgxmzdr9AJJC7","mnYoahiweETgdXsfY92GCWA6HoRj9knQUw")
    assert_equal(transfer.transfer['status'], nil)
  end

  def test_transfer_error_address
    transfer = Transfer.new("2N6uFU9UurkDgxmzdr9AJJC7","mnYoahiweETgdXsfY92GCWA6HoRj9knQUw")
    assert_equal(transfer.transfer, "Address=2N6uFU9UurkDgxmzdr9AJJC7 does not exist in your account for Network=BTCTEST.")
  end

end
