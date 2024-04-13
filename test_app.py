"""
Module to test the Flask application.
"""

import unittest
from unittest.mock import MagicMock, patch

from app import app


class TestFlaskApp(unittest.TestCase):
    """Test cases for Flask app."""

    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()

    @patch("app.expenses")
    def test_add_expense_route(self, mock_expenses):
        """Test the add_expense route."""
        mock_expenses.insert_one.return_value = MagicMock()
        response = self.app.post(
            "/add_expense",
            data={
                "description": "Test Expense",
                "category": "Test Category",
                "amount": "100.0",
                "date": "2022-01-01",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect status code

    @patch("app.expenses")
    def test_get_expenses_route(self, mock_expenses):
        """Test the get_expenses route."""
        mock_expenses.find.return_value = [
            {
                "description": "Test Expense",
                "category": "Test Category",
                "amount": 100.0,
                "date": "2022-01-01",
            }
        ]
        response = self.app.get("/get_expenses")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
