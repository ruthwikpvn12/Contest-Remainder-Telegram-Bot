import sqlite3

conn = sqlite3.connect("reminders.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sent_reminders (
    contest_name TEXT,
    reminder_type TEXT
)
""")

conn.commit()

def already_sent(contest_name, reminder_type):
    cursor.execute(
        "SELECT 1 FROM sent_reminders WHERE contest_name=? AND reminder_type=?",
        (contest_name, reminder_type)
    )
    return cursor.fetchone() is not None

def mark_sent(contest_name, reminder_type):
    cursor.execute(
        "INSERT INTO sent_reminders VALUES (?, ?)",
        (contest_name, reminder_type)
    )
    conn.commit()
