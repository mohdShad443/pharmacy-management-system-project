import sys
import os

# Ensure src directory is in python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from login import login
from medicine import medicine_menu
from billing import billing_menu

def main_menu():
    while True:
        print("\n=== PHARMACY MANAGEMENT SYSTEM ===")
        print("1. Medicine Management")
        print("2. Billing")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            medicine_menu()
        elif choice == '2':
            billing_menu()
        elif choice == '3':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("Welcome to Pharmacy Management System")
    if login():
        main_menu()
