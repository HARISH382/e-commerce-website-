import os
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Return a MySQL connection, or None if database settings are not configured."""
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "shopnova_ai"),
        )
    except Error:
        return None
