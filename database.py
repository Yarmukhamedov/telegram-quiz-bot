import sqlite3
from datetime import datetime

DB_NAME = "quiz_bot.db"

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Table for users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            total_score INTEGER DEFAULT 0,
            quizzes_completed INTEGER DEFAULT 0
        )
    ''')
    
    # Table for detailed quiz history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            score INTEGER,
            total_questions INTEGER,
            category TEXT,
            difficulty TEXT,
            timestamp DATETIME
        )
    ''')
    
    conn.commit()
    conn.close()

def update_user_stats(user_id, username, score, total_questions, category, difficulty):
    """Updates user stats and records quiz history."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Update or insert user
    cursor.execute('''
        INSERT INTO users (user_id, username, total_score, quizzes_completed)
        VALUES (?, ?, ?, 1)
        ON CONFLICT(user_id) DO UPDATE SET
            username = excluded.username,
            total_score = total_score + ?,
            quizzes_completed = quizzes_completed + 1
    ''', (user_id, username, score, score))
    
    # Record history
    cursor.execute('''
        INSERT INTO quiz_history (user_id, score, total_questions, category, difficulty, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, score, total_questions, category, difficulty, datetime.now()))
    
    conn.commit()
    conn.close()

def get_user_stats(user_id):
    """Returns total stats for a user."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT total_score, quizzes_completed FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result if result else (0, 0)

def get_top_users(limit=5):
    """Returns top users by total score."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT username, total_score FROM users ORDER BY total_score DESC LIMIT ?', (limit,))
    results = cursor.fetchall()
    conn.close()
    return results
