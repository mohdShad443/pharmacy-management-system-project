from database.db_connection import get_connection
from datetime import datetime

def generate_bill():
    customer_name = input("Enter Customer Name: ")
    cart = []
    total_amount = 0

    while True:
        med_name = input("Enter Medicine Name (or 'done' to finish): ")
        if med_name.lower() == 'done':
            break
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, price, quantity FROM medicines WHERE name = ?", (med_name,))
        med = cursor.fetchone()
        
        if med:
            med_id, price, stock = med
            qty = int(input(f"Enter Quantity (Available: {stock}): "))
            
            if qty <= stock:
                item_total = price * qty
                total_amount += item_total
                cart.append((med_id, med_name, qty, price, item_total))
                
                # Update stock
                new_stock = stock - qty
                cursor.execute("UPDATE medicines SET quantity = ? WHERE id = ?", (new_stock, med_id))
                conn.commit()
                print(f"Added to cart: {med_name} x {qty} = {item_total}")
            else:
                print("Insufficient stock!")
        else:
            print("Medicine not found!")
        conn.close()

    if cart:
        # Save Bill to DB
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bills (customer_name, total_amount) VALUES (?, ?)", (customer_name, total_amount))
        bill_id = cursor.lastrowid
        
        for item in cart:
            med_id, _, qty, price, _ = item
            cursor.execute("INSERT INTO bill_items (bill_id, medicine_id, quantity, price) VALUES (?, ?, ?, ?)", (bill_id, med_id, qty, price))
        
        conn.commit()
        conn.close()

        # Print Bill
        print("\n" + "="*30)
        print(f"PHARMACY BILL - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Customer: {customer_name}")
        print("-" * 30)
        print(f"{'Item':<15} {'Qty':<5} {'Price':<10}")
        for item in cart:
            print(f"{item[1]:<15} {item[2]:<5} {item[4]:<10}")
        print("-" * 30)
        print(f"Total Amount: {total_amount}")
        print("="*30 + "\n")
    else:
        print("Cart is empty.")

def billing_menu():
    while True:
        print("\n--- Billing Section ---")
        print("1. Generate Bill")
        print("2. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            generate_bill()
        elif choice == '2':
            break
        else:
            print("Invalid choice!")
