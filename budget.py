import sqlite3

# budget class to create and set the budget on the required category
class Budget:
    def __init__(self, user_id):
        self.user_id = user_id

    # method to set the budget for the required category
    def set_budget(self, category, amount):
        """Set a budget for a specific category."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO budgets (user_id, category, amount)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id, category) DO UPDATE SET amount = excluded.amount
        """, (self.user_id, category, amount))
        conn.commit()
        conn.close()
        print(f"Budget of {amount} set for '{category}'.")

    # method to check the budget for the required category
    def check_budget(self, category):
        """Check if the user has exceeded the budget for a category."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.amount, IFNULL(SUM(t.amount), 0) 
            FROM budgets b
            LEFT JOIN transactions t 
            ON b.user_id = t.user_id AND b.category = t.category AND t.type = 'expense'
            WHERE b.user_id = ? AND b.category = ?
        """, (self.user_id, category))
        result = cursor.fetchone()
        conn.close()

        budget, spent = result if result else (0, 0)
        if spent > budget:
            print(f"Budget exceeded for '{category}'! Spent={spent}, Budget={budget}.")
        else:
            print(f"Budget status for '{category}': Spent={spent}, Remaining={budget - spent}.")