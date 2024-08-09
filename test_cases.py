import unittest
from flask import Flask
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_get(self):
        # Test GET request to home page
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<form', result.data)  # Check if the form is in the HTML

    def test_home_post(self):
        # Test POST request with sample data
        sample_article = "This is a test article. The summarization model should summarize this."
        result = self.app.post('/', data=dict(
            article=sample_article,
            max_length=50
        ))
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Summary:', result.data)  # Check if the summary is in the HTML

if __name__ == '__main__':
    unittest.main()
