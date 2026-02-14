# Pharmacy Management System

A simple CLI-based Pharmacy Management System built with Python and SQLite.

## Features
- **User Authentication**: Secure login system.
- **Medicine Management**: Add, view, update, and delete medicines.
- **Billing**: Generate bills for customers and manage stock automatically.
- **Database**: SQLite database for persistent storage.

## Project Structure
```
Pharmacy management system/
├── database/
│   ├── pharmacy.db       # SQLite Database
│   └── (other db files)
├── src/
│   ├── database/
│   │   └── db_connection.py # Database connection logic
│   ├── billing.py        # Billing logic
│   ├── login.py          # Authentication logic
│   ├── main.py           # Application entry point
│   └── medicine.py       # Medicine management logic
├── .gitignore
└── README.md
```

## How to Run

1.  **Prerequisites**: Python 3.x installed.
2.  **Navigate to the project directory**:
    ```bash
    cd "Pharmacy management system"
    ```
3.  **Run the application**:
    ```bash
    python src/main.py
    ```
4.  **Login Credentials**:
    - **Username**: `admin`
    - **Password**: `admin123`

## Usage
- After logging in, use the menu to navigate between Medicine Management and Billing.
- Ensure you add medicines before trying to generate a bill.
