import sqlite3


def db_connect():
    conn = sqlite3.connect("goodness.db")
    print "Opened database successfully"
    return conn
