import sqlite3

DATABASE = 'car_management.db'

# Function to create tables in the database
def create_tables():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            tags TEXT,
            image_paths TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    ''')
    conn.commit()
    conn.close()

# User functions
def create_user(username, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def check_user(username):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# Car functions
def create_car(user_id, title, description, tags, image_paths):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO cars (user_id, title, description, tags, image_paths) VALUES (?, ?, ?, ?, ?)",
              (user_id, title, description, tags, image_paths))
    conn.commit()
    conn.close()

def list_cars(user_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM cars WHERE user_id = ?", (user_id,))
    cars = c.fetchall()
    conn.close()
    return cars

def search_cars(user_id, keyword):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM cars WHERE user_id = ? AND (title LIKE ? OR description LIKE ? OR tags LIKE ?)",
              (user_id, f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    cars = c.fetchall()
    conn.close()
    return cars

def update_car(car_id, title, description, tags, image_paths):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("UPDATE cars SET title = ?, description = ?, tags = ?, image_paths = ? WHERE id = ?",
              (title, description, tags, image_paths, car_id))
    conn.commit()
    conn.close()

def delete_car(car_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM cars WHERE id = ?", (car_id,))
    conn.commit()
    conn.close()
