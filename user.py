import sqlite3
import bcrypt


# user class to maintain the login register functionality of the app
class User:
    def __init__(self, username=None):
        self.username = username
        self.user_id = None


    # creation of database 'finance'
    @staticmethod
    def initialize_database():
        """Initialize the database with required tables."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                type TEXT CHECK(type IN ('income', 'expense')),
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                user_id INTEGER NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id),
                PRIMARY KEY (user_id, category)
            );
        """)

        conn.commit()
        conn.close()


    # registraion of the user
    def register(self, password):
        """Register a new user with a hashed password."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # checking whether the user exists already if not then create a new user
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, hashed_password))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("Username already exists. \n Please login")
        conn.close()

    # login of the suer
    def login(self, password):
        """Authenticate a user and set user_id if successful."""
        conn = sqlite3.connect("finance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE username = ?", (self.username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode(), result[1]):
            self.user_id = result[0]
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False
