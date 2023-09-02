## test_main.py
import unittest
from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from secure_ewallet.main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    ## Test if the FastAPI app is correctly set up
    def test_app_initialization(self):
        self.assertIsInstance(app, FastAPI)

    ## Test if the middlewares are correctly set up
    @patch('secure_ewallet.main.setup_middlewares')
    def test_setup_middlewares(self, mock_setup_middlewares):
        mock_setup_middlewares.assert_called_once_with(app)

    ## Test if the routers are correctly included
    @patch('secure_ewallet.main.app.include_router')
    def test_include_router(self, mock_include_router):
        from secure_ewallet.routers import router as api_router
        mock_include_router.assert_called_once_with(api_router)

    ## Test if the FastAPI app is running
    def test_app_running(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
