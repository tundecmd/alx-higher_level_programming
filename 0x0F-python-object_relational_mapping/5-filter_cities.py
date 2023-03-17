#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Get the command line arguments """
    username, password, database_name, state_name = argv[1:]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            charset="utf8",
            user=username,
            passwd=password,
            db=database_name
    )

    """ Prepare a cursor object using cursor() method """
    cursor = conn.cursor()

    """ Execute SQL query to fetch states """
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    """ Fetch all rows using fetchall() method """
    query_rows = cursor.fetchall()
    if query_rows is not None:
        for row in query_rows:
            print(row[0], end=",")
        print()

    """ Close the database connection """
    cursor.close()
    conn.close()
