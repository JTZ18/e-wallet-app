## test_tasks.py
import unittest
from unittest.mock import patch, MagicMock
from secure_ewallet.tasks import update_wallet_balance_task
from secure_ewallet.exceptions import WalletNotFoundException
from sqlalchemy.orm import Session

class TestTasks(unittest.TestCase):
    @patch('secure_ewallet.tasks.update_wallet_balance')
    def test_update_wallet_balance_task_success(self, mock_update_wallet_balance):
        # Mock the update_wallet_balance function to return None
        mock_update_wallet_balance.return_value = None

        # Create a mock session object
        mock_session = MagicMock(spec=Session)

        # Call the function with mock data
        update_wallet_balance_task(1, 100.0, 'credit', mock_session)

        # Assert that the mock function was called with the correct arguments
        mock_update_wallet_balance.assert_called_once_with(mock_session, 1, 100.0, 'credit')

    @patch('secure_ewallet.tasks.update_wallet_balance')
    def test_update_wallet_balance_task_wallet_not_found(self, mock_update_wallet_balance):
        # Mock the update_wallet_balance function to raise a WalletNotFoundException
        mock_update_wallet_balance.side_effect = WalletNotFoundException(detail="Wallet not found")

        # Create a mock session object
        mock_session = MagicMock(spec=Session)

        # Call the function with mock data
        with self.assertRaises(WalletNotFoundException) as context:
            update_wallet_balance_task(1, 100.0, 'credit', mock_session)

        # Assert that the exception message is correct
        self.assertTrue('Wallet not found' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
