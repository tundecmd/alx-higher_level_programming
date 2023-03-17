#!/usr/bin/python3
""" This script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Get MySQL credentials and database name from command line arguments """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    """ Connect to MySQL server """
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            charset="utf8",
            user=username,
            passwd=password,
            db=database
    )

    """ Prepare a cursor object using cursor() method """
    cursor = conn.cursor()

    """ Execute SQL query to fetch states """
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    """ Fetch all rows using fetchall() method """
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    """ Close the database connection """
    cursor.close()
    conn.close()
