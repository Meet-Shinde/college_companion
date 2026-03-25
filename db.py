#Connecting Sqlite
import csv
import sqlite3
DB_NAME="tasks.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn=get_connection() #gets connection
    cursor=conn.cursor() #from connection, gets cursor function
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT,
        created_at TEXT,
        completed INTEGER DEFAULT 0
    )
    """) #executes SQL commands
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at TEXT
    )""")
    conn.commit() #saves changes
    conn.close() #closes

def insert_task(title, due_date, created_at): #adds one row
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    INSERT INTO tasks (title, due_date, created_at)
    VALUES (?, ?, ?)
    """, (title, due_date, created_at))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks=cursor.fetchall()
    #fetchall returns a list of rows in tuple form
    #so tasks=list of tuple
    conn.close()
    return tasks

def complete_task_db(task_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    UPDATE tasks
    SET completed = 1
    WHERE id = ?
    """, (task_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    conn.close()
    return affected_rows
    #rowcount can tell if the row was found/updated/deleted.

def delete_task_db(task_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = ?
    """, (task_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    conn.close()
    return affected_rows

def get_tasks_due_between(start_date, end_date):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM tasks
    WHERE due_date BETWEEN ? AND ?
        AND completed=0
    ORDER BY due_date ASC
    """, (start_date, end_date))
    tasks=cursor.fetchall()
    conn.close()
    return tasks
    #ASC = Ascending order

def get_all_tasks_sorted():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM tasks
    ORDER BY due_date ASC
    """)
    tasks=cursor.fetchall()
    conn.close()
    return tasks

def insert_note(content, created_at):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    INSERT INTO notes (content, created_at)
    VALUES (?, ?)
    """, (content, created_at))
    conn.commit()
    conn.close()

def get_all_notes():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM notes
    ORDER BY id ASC
    """)
    notes=cursor.fetchall()
    conn.close()
    return notes

def delete_note_db(note_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    DELETE FROM notes
    WHERE id = ?
    """, (note_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    conn.close()
    return affected_rows

def export_tasks_to_csv():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM tasks
    ORDER BY due_date ASC
    """)
    tasks=cursor.fetchall()
    conn.close()
    #Creating a CSV file
    with open("tasks_export.csv", "w", newline="") as file:
        writer=csv.writer(file) #getting the writer function from csv
        writer.writerow(["id", "title", "due_date", "created_at", "completed"])
        writer.writerows(tasks)