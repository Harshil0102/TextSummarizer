import unittest
from flask import Flask
from app import app

class FlaskTestCase(unittest.TestCase):
    # Setup before each test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test for the home page
    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<html>', result.data)

    # Test for the summarize route
    def test_summarize(self):
        # Example input for summarization
        input_data = {'text': 'This is a test text for summarization.'}
        
        result = self.app.post('/summarize', json=input_data)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'summarized_text', result.data)

if __name__ == '__main__':
    unittest.main()
