import psycopg2
import json
import csv
import os
# Importing your specific variables from config.py
from config import host, user, password, db_name

def get_connection():
    """Establishes connection using your specific config variables."""
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        return conn
    except Exception as error:
        print(f"Error: Could not connect to database. {error}")
        return None

# --- 3.3 IMPORT / EXPORT LOGIC ---

def export_to_json(filename="contacts.json"):
    """Exports all contacts, phones, and groups to a JSON file."""
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()
    query = """
        SELECT c.name, c.email, c.birthday, g.name as group_name, 
               array_agg(p.phone || ':' || p.type) as phone_list
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, g.name;
    """
    try:
        cur.execute(query)
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append({
                "name": row[0],
                "email": row[1],
                "birthday": str(row[2]) if row[2] else None,
                "group": row[3],
                "phones": row[4] if row[4] and row[4][0] is not None else []
            })
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"\n[!] Successfully exported to {filename}")
    except Exception as e:
        print(f"Export error: {e}")
    finally:
        cur.close()
        conn.close()

def import_from_json(filename="contacts.json"):
    """Imports contacts from JSON with duplicate name handling."""
    if not os.path.exists(filename):
        print("File not found.")
        return
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            cur.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
            exists = cur.fetchone()
            if exists:
                choice = input(f"\nContact '{item['name']}' already exists. Overwrite? (y/n): ").lower()
                if choice != 'y': continue
                cur.execute("DELETE FROM contacts WHERE name = %s", (item['name'],))

            if item.get('group'):
                cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name RETURNING id", (item['group'],))
                group_id = cur.fetchone()[0]
            else:
                group_id = None

            cur.execute("INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                        (item['name'], item['email'], item['birthday'], group_id))
            c_id = cur.fetchone()[0]

            for p_entry in item.get('phones', []):
                if ':' in p_entry:
                    p_num, p_type = p_entry.split(':')
                    cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", (c_id, p_num, p_type))
        conn.commit()
        print("[!] JSON Import completed.")
    except Exception as e:
        conn.rollback()
        print(f"Import error: {e}")
    finally:
        cur.close()
        conn.close()

def import_from_csv(filename="contacts.csv"):
    """Imports from CSV using current fields. Handles old or new CSV formats safely."""
    if not os.path.exists(filename):
        print("CSV file not found.")
        return
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('name')
                group_name = row.get('group_name', 'Other')
                
                cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name RETURNING id", (group_name,))
                g_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id) 
                    VALUES (%s, %s, %s, %s) 
                    ON CONFLICT (name) DO UPDATE SET email=EXCLUDED.email, birthday=EXCLUDED.birthday, group_id=EXCLUDED.group_id
                    RETURNING id
                """, (name, row.get('email'), row.get('birthday'), g_id))
                c_id = cur.fetchone()[0]

                cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", 
                            (c_id, row.get('phone'), row.get('phone_type', 'mobile')))
        conn.commit()
        print("[!] CSV Data imported.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

# --- 3.2 CONSOLE INTERFACE & NAVIGATION ---

def browse_with_pagination():
    """Interactive loop for navigating pages."""
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()
    limit = 5
    offset = 0
    while True:
        cur.execute("""
            SELECT c.name, c.email, g.name, c.birthday
            FROM contacts c 
            LEFT JOIN groups g ON c.group_id = g.id 
            ORDER BY c.name LIMIT %s OFFSET %s
        """, (limit, offset))
        rows = cur.fetchall()
        print("\n--- CONTACT BOOK (Page Starting at {}) ---".format(offset + 1))
        if not rows:
            print("No contacts found on this page.")
        else:
            for r in rows:
                print(f"[{r[2] or 'No Group'}] {r[0]} - Email: {r[1]} - Bday: {r[3]}")
        cmd = input("\n[n]ext, [p]rev, [q]uit: ").lower()
        if cmd == 'n': offset += limit
        elif cmd == 'p': offset = max(0, offset - limit)
        elif cmd == 'q': break
    cur.close()
    conn.close()

def search_interface():
    """Calls the PL/pgSQL function search_contacts."""
    query = input("\nEnter search term (Name, Email, or Phone): ")
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        results = cur.fetchall()
        if not results:
            print("No matches found.")
        else:
            for r in results:
                print(f"ID: {r[0]} | Name: {r[1]} | Email: {r[2]} | Group: {r[3]}")
    except Exception as e:
        print(f"Search failed. (Ensure you ran procedures.sql): {e}")
    finally:
        cur.close()
        conn.close()

def main_menu():
    while True:
        print("\n=== PHONEBOOK SYSTEM (PRACTICE 9) ===")
        print("1. Browse Contacts (Paginated)")
        print("2. Search Contacts (Global Search)")
        print("3. Export all to JSON")
        print("4. Import from JSON")
        print("5. Import from CSV")
        print("0. Exit")
        choice = input("Select an option: ")
        if choice == '1': browse_with_pagination()
        elif choice == '2': search_interface()
        elif choice == '3': export_to_json()
        elif choice == '4': import_from_json()
        elif choice == '5': import_from_csv()
        elif choice == '0': break
        else: print("Invalid selection.")

if __name__ == "__main__":
    main_menu()