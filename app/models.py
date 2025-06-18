import sqlite3
from flask import g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('instance/budget.db')
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )''')
        db.commit()

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

def add_transaction(description, amount, date):
    db = get_db()
    db.execute('INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)',
               (description, amount, date))
    db.commit()

def get_all_transactions():
    db = get_db()
    cur = db.execute('SELECT * FROM transactions ORDER BY date DESC')
    return cur.fetchall()