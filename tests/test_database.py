"""test_database.py"""

import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from secure_ewallet.database import get_db, SessionLocal, engine

class TestDatabase(unittest.TestCase):

    ## Test get_db function
    @patch.object(SessionLocal, "__call__", return_value=MagicMock(spec=Session))
    def test_get_db(self, mock_session):
        ## Test if get_db function returns a session object
        session_gen = get_db()
        session = next(session_gen)
        self.assertIsInstance(session, Session)

        ## Test if session is closed after generator is exhausted
        with self.assertRaises(StopIteration):
            next(session_gen)
        mock_session.return_value.close.assert_called_once()

    ## Test SessionLocal settings
    def test_SessionLocal(self):
        self.assertEqual(SessionLocal.kw["autocommit"], False)
        self.assertEqual(SessionLocal.kw["autoflush"], False)
        self.assertEqual(SessionLocal.kw["bind"], engine)

    ## Test engine settings
    @patch("secure_ewallet.database.create_engine")
    def test_engine(self, mock_create_engine):
        from secure_ewallet.config import settings
        mock_create_engine.return_value = engine
        mock_create_engine.assert_called_once_with(settings.DATABASE_URL)

if __name__ == "__main__":
    unittest.main()

