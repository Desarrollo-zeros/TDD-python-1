import unittest
from fastapi.testclient import TestClient
from main import app
import requests
client = TestClient(app)

class TestMain(unittest.TestCase):
    def test_is_prime(self):
        response = client.get("/IsPrime/7")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), True)

    def test_fibonacci(self):
        response = client.get("/fibonacci/8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 21)