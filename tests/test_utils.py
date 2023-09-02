## test_utils.py

import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from fastapi import HTTPException
from secure_ewallet.models import User, Wallet, Transaction
from secure_ewallet.schemas import UserCreate, WalletCreate, TransactionCreate
from secure_ewallet.utils import get_user, get_user_by_email, get_users, create_user, get_wallet, get_wallets, create_wallet, get_transaction, get_transactions, create_transaction, check_wallet_balance, update_wallet_balance

class TestUtils(unittest.TestCase):

    ## get_user
    @patch('secure_ewallet.utils.Session')
    def test_get_user(self, mock_session):
        mock_session.query.return_value.filter.return_value.first.return_value = User(id=1)
        user = get_user(mock_session, 1)
        self.assertEqual(user.id, 1)

    ## get_user_by_email
    @patch('secure_ewallet.utils.Session')
    def test_get_user_by_email(self, mock_session):
        mock_session.query.return_value.filter.return_value.first.return_value = User(email='test@example.com')
        user = get_user_by_email(mock_session, 'test@example.com')
        self.assertEqual(user.email, 'test@example.com')

    ## get_users
    @patch('secure_ewallet.utils.Session')
    def test_get_users(self, mock_session):
        mock_session.query.return_value.offset.return_value.limit.return_value.all.return_value = [User(id=1), User(id=2)]
        users = get_users(mock_session)
        self.assertEqual(len(users), 2)

    ## create_user
    @patch('secure_ewallet.utils.Session')
    @patch('secure_ewallet.utils.get_user_by_email')
    @patch('secure_ewallet.utils.hash_password')
    def test_create_user(self, mock_hash_password, mock_get_user_by_email, mock_session):
        mock_get_user_by_email.return_value = None
        mock_hash_password.return_value = 'hashed_password'
        user_create = UserCreate(email='test@example.com', password='password', first_name='Test', last_name='User', phone_number='1234567890')
        user = create_user(mock_session, user_create)
        self.assertEqual(user.email, 'test@example.com')

    ## get_wallet
    @patch('secure_ewallet.utils.Session')
    def test_get_wallet(self, mock_session):
        mock_session.query.return_value.filter.return_value.first.return_value = Wallet(id=1)
        wallet = get_wallet(mock_session, 1)
        self.assertEqual(wallet.id, 1)

    ## get_wallets
    @patch('secure_ewallet.utils.Session')
    def test_get_wallets(self, mock_session):
        mock_session.query.return_value.offset.return_value.limit.return_value.all.return_value = [Wallet(id=1), Wallet(id=2)]
        wallets = get_wallets(mock_session)
        self.assertEqual(len(wallets), 2)

    ## create_wallet
    @patch('secure_ewallet.utils.Session')
    def test_create_wallet(self, mock_session):
        wallet_create = WalletCreate(balance=100.0)
        wallet = create_wallet(mock_session, wallet_create, 1)
        self.assertEqual(wallet.balance, 100.0)

    ## get_transaction
    @patch('secure_ewallet.utils.Session')
    def test_get_transaction(self, mock_session):
        mock_session.query.return_value.filter.return_value.first.return_value = Transaction(id=1)
        transaction = get_transaction(mock_session, 1)
        self.assertEqual(transaction.id, 1)

    ## get_transactions
    @patch('secure_ewallet.utils.Session')
    def test_get_transactions(self, mock_session):
        mock_session.query.return_value.offset.return_value.limit.return_value.all.return_value = [Transaction(id=1), Transaction(id=2)]
        transactions = get_transactions(mock_session)
        self.assertEqual(len(transactions), 2)

    ## create_transaction
    @patch('secure_ewallet.utils.Session')
    def test_create_transaction(self, mock_session):
        transaction_create = TransactionCreate(wallet_id=1, amount=100.0, transaction_type='credit')
        transaction = create_transaction(mock_session, transaction_create)
        self.assertEqual(transaction.amount, 100.0)

    ## check_wallet_balance
    @patch('secure_ewallet.utils.Session')
    @patch('secure_ewallet.utils.get_wallet')
    def test_check_wallet_balance(self, mock_get_wallet, mock_session):
        mock_get_wallet.return_value = Wallet(balance=100.0)
        self.assertTrue(check_wallet_balance(mock_session, 1, 50.0))

    ## update_wallet_balance
    @patch('secure_ewallet.utils.Session')
    @patch('secure_ewallet.utils.get_wallet')
    def test_update_wallet_balance(self, mock_get_wallet, mock_session):
        mock_get_wallet.return_value = Wallet(balance=100.0)
        wallet = update_wallet_balance(mock_session, 1, 50.0, 'debit')
        self.assertEqual(wallet.balance, 50.0)

if __name__ == '__main__':
    unittest.main()
