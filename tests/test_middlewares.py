## test_middlewares.py

import unittest
from unittest.mock import Mock, patch
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from secure_ewallet.middlewares import setup_middlewares
from secure_ewallet.config import settings

class TestMiddlewares(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        setup_middlewares(self.app)
        self.client = TestClient(self.app)

    ## Test CORS Middleware
    def test_cors_middleware(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access-control-allow-origin", response.headers)
        self.assertIn("access-control-allow-credentials", response.headers)
        self.assertIn("access-control-allow-methods", response.headers)
        self.assertIn("access-control-allow-headers", response.headers)

    ## Test Process Time Middleware
    @patch('time.time', Mock(side_effect=[1.0, 2.0]))
    def test_process_time_middleware(self):
        request = Request({"type": "http", "method": "GET", "url": "http://test"})
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("X-Process-Time", response.headers)
        self.assertEqual(response.headers["X-Process-Time"], '1.0')

    ## Test if the middleware is correctly setup
    def test_setup_middlewares(self):
        self.assertEqual(len(self.app.middleware_stack), 2)

if __name__ == "__main__":
    unittest.main()
