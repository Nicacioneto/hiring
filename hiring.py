#!/usr/bin/python3
from block_io import BlockIo, BlockIoAPIError


def inicializarAPI(_secretPIN):
	#inicializando a API
	
	version = 2 # API version
	
	bitcointTestnetApiKey = 'dac5-24ba-d04c-19f9'
	block_io = BlockIo(bitcointTestnetApiKey, _secretPIN, version)
	return block_io

def send_btc(_block_io, _amount, _fromWallet, _toWallet, _secretPIN):
	try:
		#envia 1 btc
		withdraw = _block_io.withdraw_from_addresses(amounts=_amount, 
			from_addresses=_fromWallet, to_addresses=_toWallet, pin=_secretPIN)

	except BlockIoAPIError as error:
		print(error)

	return withdraw

def main():
	secretPIN = '35kTalBneckAe'
	block_io = inicializarAPI(secretPIN)

	amount = '1.00000000'
	exampleWallet = '2N2MPfFRUmipSSdFaio23YiYw8eq6SV49qt'
	testWallet = '2MtSQLgfWpREsDjpax9k71MjiN6GRECuv2P'
	hiringWallet = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'

	withdraw = send_btc(block_io, amount, exampleWallet, hiringWallet, secretPIN)

	print("Status da operacao: ", withdraw['status'])
	print("Enviado: ", withdraw['data']['amount_sent'])

	return


if __name__ == '__main__':
	main()
