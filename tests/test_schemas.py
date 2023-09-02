import unittest
from datetime import datetime
from pydantic import ValidationError
from secure_ewallet.schemas import UserBase, UserCreate, User, WalletBase, WalletCreate, Wallet, TransactionBase, TransactionCreate, Transaction

class TestSchemas(unittest.TestCase):

    ## Test UserBase schema
    def test_user_base(self):
        with self.assertRaises(ValidationError):
            UserBase(email='notanemail', first_name='John', last_name='Doe', phone_number='1234567890')
        user_base = UserBase(email='johndoe@example.com', first_name='John', last_name='Doe', phone_number='1234567890')
        self.assertEqual(user_base.email, 'johndoe@example.com')

    ## Test UserCreate schema
    def test_user_create(self):
        with self.assertRaises(ValidationError):
            UserCreate(email='notanemail', first_name='John', last_name='Doe', phone_number='1234567890', password='')
        user_create = UserCreate(email='johndoe@example.com', first_name='John', last_name='Doe', phone_number='1234567890', password='password')
        self.assertEqual(user_create.password, 'password')

    ## Test User schema
    def test_user(self):
        with self.assertRaises(ValidationError):
            User(id='notanint', email='johndoe@example.com', first_name='John', last_name='Doe', phone_number='1234567890', is_active=True, is_superuser=False, created_at=datetime.now(), updated_at=datetime.now())
        user = User(id=1, email='johndoe@example.com', first_name='John', last_name='Doe', phone_number='1234567890', is_active=True, is_superuser=False, created_at=datetime.now(), updated_at=datetime.now())
        self.assertEqual(user.id, 1)

    ## Test WalletBase schema
    def test_wallet_base(self):
        with self.assertRaises(ValidationError):
            WalletBase(user_id='notanint')
        wallet_base = WalletBase(user_id=1)
        self.assertEqual(wallet_base.user_id, 1)

    ## Test WalletCreate schema
    def test_wallet_create(self):
        wallet_create = WalletCreate(user_id=1)
        self.assertEqual(wallet_create.user_id, 1)

    ## Test Wallet schema
    def test_wallet(self):
        with self.assertRaises(ValidationError):
            Wallet(id='notanint', user_id=1, balance='notafloat', created_at=datetime.now(), updated_at=datetime.now())
        wallet = Wallet(id=1, user_id=1, balance=100.0, created_at=datetime.now(), updated_at=datetime.now())
        self.assertEqual(wallet.id, 1)

    ## Test TransactionBase schema
    def test_transaction_base(self):
        with self.assertRaises(ValidationError):
            TransactionBase(sender_wallet_id='notanint', receiver_wallet_id='notanint', amount='notafloat')
        transaction_base = TransactionBase(sender_wallet_id=1, receiver_wallet_id=2, amount=50.0)
        self.assertEqual(transaction_base.amount, 50.0)

    ## Test TransactionCreate schema
    def test_transaction_create(self):
        transaction_create = TransactionCreate(sender_wallet_id=1, receiver_wallet_id=2, amount=50.0)
        self.assertEqual(transaction_create.amount, 50.0)

    ## Test Transaction schema
    def test_transaction(self):
        with self.assertRaises(ValidationError):
            Transaction(id='notanint', sender_wallet_id=1, receiver_wallet_id=2, amount=50.0, created_at=datetime.now())
        transaction = Transaction(id=1, sender_wallet_id=1, receiver_wallet_id=2, amount=50.0, created_at=datetime.now())
        self.assertEqual(transaction.id, 1)

if __name__ == '__main__':
    unittest.main()
