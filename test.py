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

    def test_all_code(self):
        # Validación del método IsPrime
        response = client.get("/IsPrime/7")
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json(), True)

        response = client.get("/IsPrime/6")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), False)

        response = client.get("/IsPrime/-1")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json(), False)

        response = client.get("/IsPrime/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), False)

        # Validación del método Fibonacci
        response = client.get("/fibonacci/8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 21)

        response = client.get("/fibonacci/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 1)

        response = client.get("/fibonacci/10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 55)

        response = client.get("/fibonacci/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 1)

        response = client.get("/fibonacci/-1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 1)