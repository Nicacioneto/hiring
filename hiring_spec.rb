require_relative 'hiring'

describe Transfer do 
   context "When trying to make transfer" do 
      
      it "should make a successful transfer" do 
         test_transfer = Transfer.new('2N5B2TQQNC11oSG2Tx6XSj3jWxqDmQujC15')
         expect(test_transfer.transfer).to eq "Success"
      end
      
      it "should not make a successful transfer" do 
         test_transfer = Transfer.new('2N5B2TQQNC11sfsfoG2Tx6XSj3jWxqDmQujC15')
         expect(test_transfer.transfer).to eq "Address=2N5B2TQQNC11sfsfoG2Tx6XSj3jWxqDmQujC15 does not exist in your account for Network=BTCTEST."
      end

   end
end