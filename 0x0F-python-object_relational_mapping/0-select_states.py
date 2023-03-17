#!/usr/bin/python3
""" This script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Get MySQL credentials and database name from command line arguments """
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2],
                           db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
