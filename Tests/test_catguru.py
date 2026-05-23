import os
import sys
import unittest
from unittest.mock import patch

# Dynamically add the parent directory (CatGuru) to sys.path
# This ensures api_client can be imported regardless of the working directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api_client import CatFactClient


class TestCatFactClient(unittest.TestCase):

    def test_cat_fact_client_success(self):
        """Test successful API call."""
        client = CatFactClient()
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {
                "fact": "Cats are amazing"
            }
            result = client.fetch_fact()

            # In unittest, use self.assertEqual instead of a bare assert
            self.assertEqual(result, "Cats are amazing")

    def test_cat_fact_client_timeout(self):
        """Test timeout handling."""
        client = CatFactClient()
        with patch("requests.get", side_effect=Exception("Timeout")):
            result = client.fetch_fact()

            # In unittest, use self.assertIn instead of a bare assert
            self.assertIn("Error", result)


if __name__ == "__main__":
    unittest.main()