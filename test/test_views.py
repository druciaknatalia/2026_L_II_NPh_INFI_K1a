import unittest
import json
from hello_world import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(
            {"imie": "NataliaD", "mgs": "Hello World!"},
            json.loads(rv.data)
        )

    def test_outputs(self):
        rv = self.app.get('/outputs')
        self.assertIn(b'plain', rv.data)