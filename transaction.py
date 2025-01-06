import sqlite3
import datetime


# trancation class for managing the trancationa and updating the data into the db
class Transaction:
    def __init__(self, user_id):
        self.user_id = user_id

    # function to add a tranction 
    def add_transaction(self, type, category, amount, date=None):
        """Add a new transaction."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        date = date or datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
            INSERT INTO transactions (user_id, type, category, amount, date)
            VALUES (?, ?, ?, ?, ?)
        """, (self.user_id, type, category, amount, date))
        conn.commit()
        conn.close()
        print(f"{type.capitalize()} of {amount} added under '{category}' on {date}.")

    # function to generate a report for the given year and month
    def generate_report(self, year, month=None):
        """Generate monthly or yearly financial report."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        query = "SELECT type, SUM(amount) FROM transactions WHERE user_id = ? AND strftime('%Y', date) = ?"
        params = [self.user_id, year]
        if month:
            query += " AND strftime('%m', date) = ?"
            params.append(f"{int(month):02d}")
        query += " GROUP BY type"
        cursor.execute(query, params)
        data = cursor.fetchall()
        conn.close()

        income = sum(amount for t, amount in data if t == "income")
        expense = sum(amount for t, amount in data if t == "expense")
        print(f"Report for {year}-{month or 'All'}: Income={income}, Expense={expense}, Savings={income - expense}")

