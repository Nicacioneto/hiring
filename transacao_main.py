from transacao import Transacao
import os

api_key = os.environ['BLOCKIO_API_KEY']
pin = os.environ['BLOCKIO_PIN']
destiny_wallet = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'
source_wallet = '2N1Sc7EKejrGiWceitFmXrAorZtfHs3pCxb'
api_version = 2
amount = '1'

t = Transacao(        
    api_key,
    pin,
    destiny_wallet,
    source_wallet,
    api_version,
    amount
)

block = t.setup()
balance = t.check_balance(block)
print(balance)
withdrawal = t.send_cryptocoin(block, amount, source_wallet, destiny_wallet)
print(withdrawal)