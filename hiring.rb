require 'block_io'

class Transfer

	def initialize(from)
		@from = from
	end

	def transfer
		begin
			BlockIo.set_options :api_key => "1ddb-7fde-299d-b0df", :pin => "beachcoin" , :version => 2
	        BlockIo.withdraw_from_addresses :amounts => '1.0', :from_addresses => @from, :to_addresses => 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'
	        return "Success"
	    rescue Exception => e
	    	puts e.message
	    	return e.message
	    end
	end
end

tranfertest = Transfer.new('2N5B2TQQNC11oSG2Tx6XSj3jWxqDmQujC15')
tranfertest.transfer()
