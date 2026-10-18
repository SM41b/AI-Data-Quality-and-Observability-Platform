from src.database.connection import get_connection

def main():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT current_database(), current_user')
            result = cursor.fetchone()
    print(f'Connected successfully: database = {result[0]}, user = {result[1]}.')

if __name__=='__main__':
    main()