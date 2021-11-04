import requests
import mysql.connector

def execute() {
    configure()
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True)
    
}

def configure() {
    config = {
        'user': '',
        'password': '',
        'host': '',
        'database': ''
    }
}

def close_connection() {
    connection.close()
}

def close_cursor() {
    cursor.close()
}