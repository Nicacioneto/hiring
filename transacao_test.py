from transacao import Transacao
from decimal import Decimal

import six # for python2 back-compatibility in printing messages using print as a function
import os
import unittest
import time

API_KEY = os.environ['BLOCKIO_API_KEY']
PIN = os.environ['BLOCKIO_PIN']
SOURCE_WALLET = os.environ['SOURCE_WALLET']'
DESTINY_WALLET = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'
API_VERSION = 2
AMOUNT = '0.00001'
NETWORK_FEE = '0.00001944'

if (API_KEY is None) or (PIN is None):
    raise Exception("NEED env: BLOCKIO_API_KEY && BLOCKIO_PIN")

transaction_block = Transacao(        
    API_KEY,
    PIN,
    DESTINY_WALLET,
    SOURCE_WALLET,
    API_VERSION,
    AMOUNT
)

block_io = transaction_block.setup()

class BlockIoAPITest(unittest.TestCase):
    def setUp(self):
        self.client = block_io

    def result_assertions(self, result):
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result["data"], dict)
        self.assertEqual(result["status"], "success")
        self.assertNotIn("error", result)

class TestBasic(BlockIoAPITest):
    def test_get_balance(self):
        self.assertNotEqual(block_io, "")

        result = transaction_block.check_balance(block_io)

        self.result_assertions(result)

class TestWithdraw(BlockIoAPITest):

    def test_withdraw(self):
        self.assertNotEqual(DESTINY_WALLET, "")
        self.assertNotEqual(SOURCE_WALLET, "")
        self.assertNotEqual(AMOUNT, "")
        self.assertNotEqual(block_io, "")
        
        result = transaction_block.send_cryptocoin(block_io, AMOUNT, SOURCE_WALLET, DESTINY_WALLET)
        
        self.result_assertions(result)

        self.assertEqual(Decimal(result["data"]["network_fee"]), Decimal(NETWORK_FEE))
        self.assertEqual(Decimal(result["data"]["blockio_fee"]), Decimal(0))
        self.assertEqual(Decimal(result["data"]["amount_sent"]), Decimal(AMOUNT))
        
        NETWORK_FEE2 = Decimal(NETWORK_FEE)
        AMOUNT2 = Decimal(AMOUNT)
        total_value = NETWORK_FEE2 + AMOUNT2
        self.assertEqual(Decimal(result["data"]["amount_withdrawn"]), total_value)
        self.assertIsInstance(result["data"]["txid"], six.text_type)

basicTest = unittest.TestLoader().loadTestsFromTestCase(TestBasic)
witdrawTest = unittest.TestLoader().loadTestsFromTestCase(TestWithdraw)

# Runner
print("TESTING BLOCK-IO, api: v{av}; client: v{cv}".format(av=block_io.version, cv=block_io.clientVersion))
unittest.TextTestRunner(verbosity=2).run(basicTest)
unittest.TextTestRunner(verbosity=2).run(witdrawTest)
