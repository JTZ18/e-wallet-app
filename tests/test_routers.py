import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from secure_ewallet.main import app
from secure_ewallet.schemas import UserCreate, WalletCreate, TransactionCreate
from secure_ewallet.database import get_db
from secure_ewallet.auth import get_current_active_user

class TestRouters(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.user_create = UserCreate(email='test@test.com', password='test123')
        self.wallet_create = WalletCreate(balance=1000.0)
        self.transaction_create = TransactionCreate(sender_wallet_id=1, receiver_wallet_id=2, amount=100.0)

    ## Test User Routes
    @patch('secure_ewallet.routers.create_user')
    def test_create_user_route(self, mock_create_user):
        response = self.client.post("/users", json=self.user_create.dict())
        self.assertEqual(response.status_code, 201)
        mock_create_user.assert_called()

    @patch('secure_ewallet.routers.get_users')
    def test_read_users(self, mock_get_users):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        mock_get_users.assert_called()

    @patch('secure_ewallet.routers.get_user')
    def test_read_user(self, mock_get_user):
        mock_get_user.return_value = None
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 404)

    ## Test Wallet Routes
    @patch('secure_ewallet.routers.create_wallet')
    @patch('secure_ewallet.routers.get_current_active_user')
    def test_create_wallet_route(self, mock_get_current_active_user, mock_create_wallet):
        mock_get_current_active_user.return_value = MagicMock(id=1)
        response = self.client.post("/wallets", json=self.wallet_create.dict())
        self.assertEqual(response.status_code, 201)
        mock_create_wallet.assert_called()

    @patch('secure_ewallet.routers.get_wallets')
    def test_read_wallets(self, mock_get_wallets):
        response = self.client.get("/wallets")
        self.assertEqual(response.status_code, 200)
        mock_get_wallets.assert_called()

    @patch('secure_ewallet.routers.get_wallet')
    def test_read_wallet(self, mock_get_wallet):
        mock_get_wallet.return_value = None
        response = self.client.get("/wallets/1")
        self.assertEqual(response.status_code, 404)

    ## Test Transaction Routes
    @patch('secure_ewallet.routers.create_transaction')
    @patch('secure_ewallet.routers.check_wallet_balance')
    @patch('secure_ewallet.routers.update_wallet_balance')
    def test_create_transaction_route(self, mock_update_wallet_balance, mock_check_wallet_balance, mock_create_transaction):
        mock_check_wallet_balance.return_value = True
        response = self.client.post("/transactions", json=self.transaction_create.dict())
        self.assertEqual(response.status_code, 201)
        mock_create_transaction.assert_called()
        mock_update_wallet_balance.assert_called()

    @patch('secure_ewallet.routers.get_transactions')
    def test_read_transactions(self, mock_get_transactions):
        response = self.client.get("/transactions")
        self.assertEqual(response.status_code, 200)
        mock_get_transactions.assert_called()

    @patch('secure_ewallet.routers.get_transaction')
    def test_read_transaction(self, mock_get_transaction):
        mock_get_transaction.return_value = None
        response = self.client.get("/transactions/1")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
