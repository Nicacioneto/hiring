import os
from block_io import BlockIo

class Transacao:
    
    def __init__(self,api_key,pin,source_wallet,destiny_wallet,api_version,amount):
        self.api_key = api_key
        self.pin = pin
        self.source_wallet = source_wallet
        self.destiny_wallet = destiny_wallet
        self.api_version = api_version
        self.amount = amount

    def setup(self):
        block_io = BlockIo(self.api_key, self.pin, self.api_version)
        return block_io

    def check_balance(self, block_io):
        balance = block_io.get_balance()
        return balance

    def send_cryptocoin(self, block_io, amount, source_wallet, destiny_wallet):
        transaction = block_io.withdraw_from_addresses(amounts=amount, from_addresses=source_wallet, to_addresses=destiny_wallet)
        return transaction