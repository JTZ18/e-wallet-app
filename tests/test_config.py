"""
test_config.py
"""

import unittest
from secure_ewallet.config import Settings

class TestConfig(unittest.TestCase):
    ## Test Default Values
    def test_default_values(self):
        settings = Settings()
        self.assertEqual(settings.DATABASE_URL, "sqlite:///./test.db")
        self.assertEqual(settings.SECRET_KEY, "YOUR_SECRET_KEY")
        self.assertEqual(settings.ALGORITHM, "HS256")
        self.assertEqual(settings.ACCESS_TOKEN_EXPIRE_MINUTES, 30)
        self.assertEqual(settings.STRIPE_API_KEY, "YOUR_STRIPE_API_KEY")
        self.assertEqual(settings.REDIS_URL, "redis://localhost:6379/0")
        self.assertEqual(settings.CELERY_BROKER_URL, "pyamqp://guest@localhost//")
        self.assertEqual(settings.SENTRY_DSN, "YOUR_SENTRY_DSN")
        self.assertEqual(settings.MKDOCS_CONFIG_FILE, "mkdocs.yml")
        self.assertEqual(settings.DOCKERFILE, "Dockerfile")
        self.assertEqual(settings.KUBERNETES_CONFIG_FILE, "k8s_config.yml")
        self.assertEqual(settings.FLOWER_PORT, 5555)
        self.assertEqual(settings.FLOWER_URL_PREFIX, "flower")
        self.assertEqual(settings.FLOWER_BASIC_AUTH, "user:password")

    ## Test Set Values
    def test_set_values(self):
        settings = Settings(DATABASE_URL="sqlite:///./new_test.db", SECRET_KEY="NEW_SECRET_KEY")
        self.assertEqual(settings.DATABASE_URL, "sqlite:///./new_test.db")
        self.assertEqual(settings.SECRET_KEY, "NEW_SECRET_KEY")

    ## Test Invalid Values
    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            settings = Settings(ACCESS_TOKEN_EXPIRE_MINUTES="invalid")

if __name__ == '__main__':
    unittest.main()
