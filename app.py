from flask import Flask, render_template, request, redirect, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Initialize Flask application
app = Flask(__name__)

load_dotenv()

uri = os.environ.get("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['expense_tracker']
# Expense collection
expenses = db.expenses

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route('/')
def index():
    all_expenses = list(expenses.find())
    return render_template('index.html', expenses=all_expenses)


@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = {
        'description': request.form.get('description'),
        'category': request.form.get('category'),
        'amount': float(request.form.get('amount')),
        'date': request.form.get('date')
    }
    expenses.insert_one(expense)
    return redirect(url_for('index'))


@app.route('/get_expenses')
def get_expenses():
    all_expenses = list(expenses.find())
    return render_template('expenses.html', expenses=all_expenses)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
