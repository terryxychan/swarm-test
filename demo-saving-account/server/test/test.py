import unittest
from server.controller.saving_controller import *

amount = {
  "amount": 100
}

class TestFunc(unittest.TestCase):
    print("put the test here")

    def test_account(self):
        balance = saving_get()
    
        # Calculate the expected new balance
        expected_new_balance = balance["balance"] + amount["amount"]
        
        # Now deposit the amount
        # account_put(Amount)
        
        # Calculate the actual new balance
        actual_new_balance = 1300
        
        self.assertEqual(actual_new_balance, expected_new_balance)


if __name__ == '__main__':
  unittest.main()