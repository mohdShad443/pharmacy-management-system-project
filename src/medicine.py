from database.db_connection import get_connection

def add_medicine():
    name = input("Enter Medicine Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO medicines (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
        conn.commit()
        print("Medicine added successfully!")
    except Exception as e:
        print(f"Error adding medicine: {e}")
    finally:
        conn.close()

def view_medicines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()
    conn.close()

    print("\n--- Medicine List ---")
    print(f"{'ID':<5} {'Name':<20} {'Qty':<10} {'Price'}")
    print("-" * 45)
    for med in medicines:
        print(f"{med[0]:<5} {med[1]:<20} {med[2]:<10} {med[3]}")
    print("-" * 45)

def update_medicine():
    view_medicines()
    med_id = int(input("Enter Medicine ID to Update: "))
    new_qty = int(input("Enter New Quantity: "))
    new_price = float(input("Enter New Price: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE medicines SET quantity = ?, price = ? WHERE id = ?", (new_qty, new_price, med_id))
    conn.commit()
    conn.close()
    print("Medicine updated successfully!")

def delete_medicine():
    view_medicines()
    med_id = int(input("Enter Medicine ID to Delete: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medicines WHERE id = ?", (med_id,))
    conn.commit()
    conn.close()
    print("Medicine deleted successfully!")

def medicine_menu():
    while True:
        print("\n--- Medicine Management ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            update_medicine()
        elif choice == '4':
            delete_medicine()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
