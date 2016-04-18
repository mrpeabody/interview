import unittest
from flask_testing import LiveServerTestCase
from problem2 import app
import requests


class Problem2Test(LiveServerTestCase):
    """
    This class encapsulates tests for the problem2 web app
    """
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000

        return app

    def test_successful_response(self):
        self.assertEqual(requests.get(self.get_server_url() + '/comment/100').status_code, 200)

    def test_non_existing_comment_id(self):
        self.assertEqual(requests.get(self.get_server_url() + '/comment/999').status_code, 404)

    def test_nonexisting_url(self):
        self.assertEqual(requests.get(self.get_server_url() + '/non_existing').status_code, 404)

    def test_non_get_request(self):
        """
        The comment URL only supports GET. Other requests should return 405 (NOT ALLOWED)
        """
        self.assertEqual(requests.post(self.get_server_url() + '/comment/100').status_code, 405)
        self.assertEqual(requests.put(self.get_server_url() + '/comment/100').status_code, 405)
        self.assertEqual(requests.delete(self.get_server_url() + '/comment/100').status_code, 405)

if __name__ == '__main__':
    unittest.main()
