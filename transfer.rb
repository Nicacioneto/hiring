require 'block_io'

class Transfer

  $api_key ="5d81-dedd-3eb9-552d"
  $pin ="iamhopesandman"

  def initialize(from, to)
    @from = from
    @to = to
  end

  def transfer
    begin
      BlockIo.set_options :api_key=>$api_key, :pin =>$pin, :version => 2
      BlockIo.withdraw :amounts => '0.1', :to_addresses => @to, :from_addresses => @from
    rescue Exception => e
     return e.message
   end
  end

end


transferClass = Transfer.new("2NGAyhPa8EqoE6uFU9UurkDgxmzdr9AJJC7","mnYoahiweETgdXsfY92GCWA6HoRj9knQUw")
transferClass.transfer()
