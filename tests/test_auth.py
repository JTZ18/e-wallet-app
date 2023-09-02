## test_auth.py

import unittest
from unittest.mock import patch, MagicMock
from datetime import timedelta
from sqlalchemy.orm import Session
from jose import JWTError

from secure_ewallet.auth import hash_password, verify_password, authenticate_user, create_access_token, get_current_user, get_current_active_user
from secure_ewallet.models import User
from secure_ewallet.schemas import User as UserSchema
from secure_ewallet.config import settings

class TestAuth(unittest.TestCase):

    ## Test hash_password function
    def test_hash_password(self):
        password = "test_password"
        hashed_password = hash_password(password)
        self.assertTrue(verify_password(password, hashed_password))

    ## Test verify_password function
    def test_verify_password(self):
        password = "test_password"
        hashed_password = hash_password(password)
        self.assertTrue(verify_password(password, hashed_password))
        self.assertFalse(verify_password("wrong_password", hashed_password))

    ## Test authenticate_user function
    @patch.object(Session, 'query')
    def test_authenticate_user(self, mock_query):
        email = "test@test.com"
        password = "test_password"
        hashed_password = hash_password(password)
        mock_user = User(email=email, password=hashed_password)
        mock_query.return_value.filter.return_value.first.return_value = mock_user
        db = Session()
        user = authenticate_user(db, email, password)
        self.assertEqual(user, mock_user)

    ## Test create_access_token function
    def test_create_access_token(self):
        data = {"sub": "test@test.com"}
        token = create_access_token(data)
        self.assertIsInstance(token, str)

    ## Test get_current_user function
    @patch.object(Session, 'query')
    @patch('secure_ewallet.auth.jwt.decode')
    def test_get_current_user(self, mock_decode, mock_query):
        token = "test_token"
        email = "test@test.com"
        mock_decode.return_value = {"sub": email}
        mock_user = User(email=email)
        mock_query.return_value.filter.return_value.first.return_value = mock_user
        db = Session()
        user = get_current_user(token, db)
        self.assertEqual(user, mock_user)

    ## Test get_current_active_user function
    @patch('secure_ewallet.auth.get_current_user')
    def test_get_current_active_user(self, mock_get_current_user):
        mock_user = UserSchema(is_active=True)
        mock_get_current_user.return_value = mock_user
        user = get_current_active_user(mock_user)
        self.assertEqual(user, mock_user)

if __name__ == "__main__":
    unittest.main()
