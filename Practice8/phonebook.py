import psycopg2
from connect import get_connection

# 1. Calls the Upsert procedure
def add_or_update_user(name, phone):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        # Using CALL for procedures
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Processed contact: {name}")

# 2. Calls the Bulk Insert procedure
def bulk_insert(names_list, phones_list):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        # We pass arrays and one NULL for the OUT parameter
        cur.execute("CALL insert_many_users(%s, %s, NULL)", (names_list, phones_list))
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if result and result[0]:
            print(f"Validation errors (skipped): {result[0]}")
        else:
            print("Bulk insert finished with no errors.")

# 3. Calls the Search function
def search_contacts(pattern):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        # Using SELECT for functions
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
        rows = cur.fetchall()
        print(f"\n--- Search results for '{pattern}' ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
        cur.close()
        conn.close()

# 4. Calls the Pagination function
def show_paged(limit, offset):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts_paged(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        print(f"\n--- Paged data (Limit: {limit}, Offset: {offset}) ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
        cur.close()
        conn.close()

# 5. Calls the Delete procedure
def remove_contact(target):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("CALL delete_contact_by_data(%s)", (target,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Delete procedure executed for: {target}")

if __name__ == "__main__":
    # Test 1: Add or Update
    add_or_update_user("Madi", "87771112233")
    
    # Test 2: Bulk Insert (one valid, one too short)
    bulk_insert(["User1", "User2"], ["87019998877", "123"]) 
    
    # Test 3: Search
    search_contacts("Ma")
    
    # Test 4: Pagination
    show_paged(5, 0)
    
    # Test 5: Delete
    remove_contact("User1")