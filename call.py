from connect import connect

cursor = connect.connect()
connect.close_connection(cursor)