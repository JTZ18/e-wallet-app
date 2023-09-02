## test_exceptions.py
import unittest
from secure_ewallet.exceptions import InsufficientBalanceException, WalletNotFoundException, UserNotFoundException, TransactionNotFoundException

class TestExceptions(unittest.TestCase):
    def test_insufficient_balance_exception(self):
        try:
            raise InsufficientBalanceException()
        except InsufficientBalanceException as e:
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.detail, "Insufficient balance in the wallet")

    def test_wallet_not_found_exception(self):
        try:
            raise WalletNotFoundException()
        except WalletNotFoundException as e:
            self.assertEqual(e.status_code, 404)
            self.assertEqual(e.detail, "Wallet not found")

    def test_user_not_found_exception(self):
        try:
            raise UserNotFoundException()
        except UserNotFoundException as e:
            self.assertEqual(e.status_code, 404)
            self.assertEqual(e.detail, "User not found")

    def test_transaction_not_found_exception(self):
        try:
            raise TransactionNotFoundException()
        except TransactionNotFoundException as e:
            self.assertEqual(e.status_code, 404)
            self.assertEqual(e.detail, "Transaction not found")

if __name__ == "__main__":
    unittest.main()
