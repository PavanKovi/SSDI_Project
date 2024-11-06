from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing

# Example class for User and Expense, simulating a database
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Expense:
    def __init__(self, id, user_id, amount, category, date):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.date = date

# In-memory storage to simulate a database
users_db = {}
expenses_db = {}

# Simulate database tables for Users and Expenses
def create_user(username, password):
    user_id = len(users_db) + 1
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(user_id, username, hashed_password)
    users_db[username] = new_user
    return new_user

def create_expense(user_id, amount, category):
    expense_id = len(expenses_db) + 1
    new_expense = Expense(expense_id, user_id, amount, category, datetime.utcnow())
    expenses_db[expense_id] = new_expense
    return new_expense

# Simulate login (session management removed for simplicity)
def login(username, password):
    user = users_db.get(username)
    if user and check_password_hash(user.password, password):
        return user
    else:
        return None

# Simulate user registration
def register(username, password):
    if username not in users_db:
        return create_user(username, password)
    else:
        return None

# Simulate dashboard view (without Flask templating)
def dashboard(user_id):
    user_expenses = [expense for expense in expenses_db.values() if expense.user_id == user_id]
    return user_expenses

# Simulate logging out
def logout():
    print("You have been logged out.")
    return None

# Example usage of the system
# Register new users
new_user = register("john_doe", "password123")
if new_user:
    print(f"User {new_user.username} registered successfully!")

# Login
user = login("john_doe", "password123")
if user:
    print(f"Welcome {user.username}!")
    # Add an expense
    create_expense(user.id, 50.0, "Groceries")
    create_expense(user.id, 100.0, "Utilities")
    # Show dashboard
    expenses = dashboard(user.id)
    print("Expenses:", [f"{expense.category}: ${expense.amount}" for expense in expenses])
else:
    print("Login failed.")

# Logout
logout()
