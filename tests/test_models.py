## test_models.py
import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secure_ewallet.models import User, Wallet, Transaction
from secure_ewallet.database import Base

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    ## Test User Model
    def test_create_user(self):
        user = User(email='test@example.com', password='password', first_name='Test', last_name='User', phone_number='1234567890')
        self.session.add(user)
        self.session.commit()

        queried_user = self.session.query(User).filter_by(email='test@example.com').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'test@example.com')
        self.assertEqual(queried_user.password, 'password')
        self.assertEqual(queried_user.first_name, 'Test')
        self.assertEqual(queried_user.last_name, 'User')
        self.assertEqual(queried_user.phone_number, '1234567890')
        self.assertTrue(isinstance(queried_user.created_at, datetime))
        self.assertTrue(isinstance(queried_user.updated_at, datetime))
        self.assertTrue(queried_user.is_active)
        self.assertFalse(queried_user.is_superuser)

    ## Test Wallet Model
    def test_create_wallet(self):
        user = User(email='test@example.com', password='password', first_name='Test', last_name='User', phone_number='1234567890')
        self.session.add(user)
        self.session.commit()

        wallet = Wallet(user_id=user.id)
        self.session.add(wallet)
        self.session.commit()

        queried_wallet = self.session.query(Wallet).filter_by(user_id=user.id).first()
        self.assertIsNotNone(queried_wallet)
        self.assertEqual(queried_wallet.user_id, user.id)
        self.assertEqual(queried_wallet.balance, 0)
        self.assertTrue(isinstance(queried_wallet.created_at, datetime))
        self.assertTrue(isinstance(queried_wallet.updated_at, datetime))

    ## Test Transaction Model
    def test_create_transaction(self):
        sender = User(email='sender@example.com', password='password', first_name='Sender', last_name='User', phone_number='1234567890')
        receiver = User(email='receiver@example.com', password='password', first_name='Receiver', last_name='User', phone_number='1234567890')
        self.session.add(sender)
        self.session.add(receiver)
        self.session.commit()

        sender_wallet = Wallet(user_id=sender.id)
        receiver_wallet = Wallet(user_id=receiver.id)
        self.session.add(sender_wallet)
        self.session.add(receiver_wallet)
        self.session.commit()

        transaction = Transaction(sender_wallet_id=sender_wallet.id, receiver_wallet_id=receiver_wallet.id, amount=100)
        self.session.add(transaction)
        self.session.commit()

        queried_transaction = self.session.query(Transaction).filter_by(sender_wallet_id=sender_wallet.id).first()
        self.assertIsNotNone(queried_transaction)
        self.assertEqual(queried_transaction.sender_wallet_id, sender_wallet.id)
        self.assertEqual(queried_transaction.receiver_wallet_id, receiver_wallet.id)
        self.assertEqual(queried_transaction.amount, 100)
        self.assertTrue(isinstance(queried_transaction.created_at, datetime))

if __name__ == '__main__':
    unittest.main()
