import psycopg2
from config import host, user, password, db_name

def get_connection():
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        return conn
    except Exception as error:
        print("Error: Could not connect to database.")
        return None