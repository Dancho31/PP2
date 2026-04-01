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
        print(f"Ошибка при подключении к базе данных: {error}")
        return None

# Проверка связи
if __name__ == "__main__":
    connection = get_connection()
    if connection:
        print("Победа! Мы подключились к базе.")
        connection.close()