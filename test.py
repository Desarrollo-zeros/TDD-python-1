import unittest
from fastapi.testclient import TestClient
from main import app
import requests
client = TestClient(app)
