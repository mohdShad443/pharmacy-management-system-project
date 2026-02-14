from database.db_connection import get_connection

def login():
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Login successful! Welcome, {username}.")
        return True
    else:
        print("Invalid username or password.")
        return False
