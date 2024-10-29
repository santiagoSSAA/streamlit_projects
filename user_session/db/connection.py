import sqlite3

def create_connection():
    return sqlite3.connect('users.db') 