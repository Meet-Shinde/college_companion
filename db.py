#Connecting Sqlite
import sqlite3
DB_NAME="tasks.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn=get_connection() #gets connection
    cursor=conn.cursor() #from connection, gets cursor function
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT,
        created_at TEXT,
        completed INTEGER DEFAULT 0
    )
    ''') #executes SQL commands
    conn.commit() #saves changes
    conn.close #closes

def insert_tasks(title, due_date, created_at): #adds one row
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (title, due_date, created_at)
    VALUES (?, ?, ?)
    ''', (title, due_date, created_at))
    conn.commit
    conn.close

def get_all_tasks():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * from tasks")
    tasks=cursor.fetchall()
    #fetchall returns a list of rows in tuple form
    #so tasks=list of tuple
    conn.close()
    return tasks