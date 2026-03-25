
import csv
import psycopg2
from connect import get_connection

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        contact_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """
    conn = get_connection()
    if conn:
        curr = conn.cursor()
        curr.execute(sql)
        conn.commit() 
        curr.close()
        conn.close()
        print("System ready: Table 'phonebook' is verified.")

# 1. Add a single contact manually
def insert_contact(name, phone):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Contact '{name}' has been saved!")

# 2. Upload contacts from a CSV file
def upload_from_csv(file_path):
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    # row[0] is name, row[1] is phone
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            cur.close()
            print("Data from CSV imported successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

# 3. Query contacts with optional filter
def get_contacts(filter_name=None):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        if filter_name:
            # ILIKE is case-insensitive search
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{filter_name}%",))
        else:
            cur.execute("SELECT * FROM phonebook")
        
        rows = cur.fetchall()
        print("\n--- PhoneBook Contacts ---")
        if not rows:
            print("No contacts found.")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
        cur.close()
        conn.close()

# 4. Delete a contact by name or phone
def delete_contact(target):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (target, target))
        conn.commit()
        count = cur.rowcount # check how many rows were deleted
        cur.close()
        conn.close()
        if count > 0:
            print(f"Contact '{target}' deleted successfully.")
        else:
            print(f"No contact found with name/phone: {target}")

# MAIN MENU
if __name__ == "__main__":
    create_table()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Show all contacts")
        print("2. Add contact manually")
        print("3. Upload from CSV (contacts.csv)")
        print("4. Search contact by name")
        print("5. Delete contact")
        print("0. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            get_contacts()
        elif choice == '2':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            insert_contact(name, phone)
        elif choice == '3':
            upload_from_csv('contacts.csv')
        elif choice == '4':
            name = input("Enter name to search: ")
            get_contacts(name)
        elif choice == '5':
            target = input("Enter name or phone to delete: ")
            delete_contact(target)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")