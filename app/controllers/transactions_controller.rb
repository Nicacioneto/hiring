class TransactionsController < ApplicationController
	def new
		# chave da carteira de BTC do block.io
		# Essa chave deve variar de acordo com a conta que está transferindo e o tipo de altcoin
		api_key_btc = '74b0-1818-a7ef-8cde'
		# api_key_btc: Responsável por dar um set na carteira do proprietário, modificando também o tipo da altcoin
		# pin: Chave gerada na criação de contas no Block.io 
		# version: versão de uso da api do Block.io 
		BlockIo.set_options :api_key=> api_key_btc,:pin=>'12345678', :version => 2
		return new_withdraw('mnYoahiweETgdXsfY92GCWA6HoRj9knQUw', 1.0)
    end

    private 
    #Responsável por realizar a transferência de valores
    def new_withdraw(address, value)
        return BlockIo.withdraw :amounts => value, :to_addresses => address
    end
end
