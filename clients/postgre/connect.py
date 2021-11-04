import psycopg2
from config import config

def connect():
    conn = None

    try:

        #read config params
        param = config()

        #connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**param)

        #create a cursor
        cursor = conn.cursor

        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        return cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def close_connection(cursor):
    print('Database connection closed.')
    cursor.close()
