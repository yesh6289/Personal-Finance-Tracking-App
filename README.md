# Personal-Finance-Tracking-App

# Personal Finance Management Application

A Python-based personal finance management app that allows users to track expenses, set budgets, and manage transactions efficiently. It supports user registration, login, and provides detailed financial reports.

---

## Features

- **User Registration and Login**: 
  - Secure user authentication with hashed passwords.
  - User data stored in an SQLite database.

- **Transactions Management**: 
  - Add and categorize transactions (income/expense).
  - Generate detailed financial reports for any month or year.

- **Budgeting**: 
  - Set budgets for specific categories.
  - Track spending and check if budgets are exceeded.

---

## Project Structure

```plaintext
.
├── app.py         # Main application file
├── user.py        # Handles user registration and login
├── transaction.py # Manages transactions and reporting
├── budget.py      # Manages budgets and budget checks
├── finance.db     # SQLite database (created automatically when the app runs)

```
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/<your-username>/personal-finance-app.git
cd personal-finance-app
Install dependencies:

Ensure you have Python 3.7 or later installed.
Install bcrypt for secure password hashing:
bash
Copy code
pip install bcrypt
Run the application:

bash
Copy code
python app.py
Usage
Start the App:

Run app.py to launch the application.
Follow the menu options for registration, login, and managing finances.
Set Budgets:

Use the "Set Budget" feature to define budgets for specific categories.
Track Spending:

Add income and expense transactions and check budget statuses.
Generate Reports:

Generate detailed reports for a specific month or year.
Technologies Used
Python: Core programming language.
SQLite: Lightweight database for storing user, transaction, and budget data.
bcrypt: Secure password hashing library.
Example Workflow
Register a User:
Enter a username and password to create an account.
Login:
Use your credentials to log in.
Add Transactions:
Add income or expense transactions with categories and amounts.
Set Budgets:
Define budgets for different spending categories.
Generate Reports:
View detailed reports on income, expenses, and savings.
Future Enhancements
Add data visualization for reports.
Integrate cloud storage for data backup.
Build a web or mobile interface for broader accessibility.
Contributing
Contributions are welcome! Feel free to submit a pull request or file an issue for bugs or feature suggestions.


![Screenshot 2025-01-06 210349](https://github.com/user-attachments/assets/ccc82fbe-c102-4f3d-9b08-4e9d70a596aa)
