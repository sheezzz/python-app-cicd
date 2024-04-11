"""
Flask application for expense tracking.
"""

import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Initialize Flask application
app = Flask(__name__)

load_dotenv()

uri = os.environ.get("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["expense_tracker"]
# Expense collection
expenses = db.expenses

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except ConnectionError as conn_err:
    print(f"ConnectionError: {conn_err}")
except TimeoutError as timeout_err:
    print(f"TimeoutError: {timeout_err}")
except Exception as generic_err:
    print(f"An unexpected error occurred: {generic_err}")


@app.route("/")
def index():
    """
    Render the index page with a list of all expenses.

    Returns:
        flask.render_template: Rendered HTML template.
    """
    all_expenses = list(expenses.find())
    return render_template("index.html", expenses=all_expenses)


@app.route("/add_expense", methods=["POST"])
def add_expense():
    """
    Add a new expense to the database.

    Returns:
        flask.redirect: Redirect to the index page.
    """
    expense = {
        "description": request.form.get("description"),
        "category": request.form.get("category"),
        "amount": float(request.form.get("amount")),
        "date": request.form.get("date"),
    }
    expenses.insert_one(expense)
    return redirect(url_for("index"))


@app.route("/get_expenses")
def get_expenses():
    """
    Retrieve all expenses from the database.

    Returns:
        flask.render_template: Rendered HTML template.
    """
    all_expenses = list(expenses.find())
    return render_template("expenses.html", expenses=all_expenses)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
