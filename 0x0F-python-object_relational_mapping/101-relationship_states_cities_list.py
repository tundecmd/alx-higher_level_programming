#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check that the script is being called correctly
    if (len(sys.argv) != 4):
        print("Usage: {} username password db_name".format(sys.argv[0]))
        sys.exit(1)

    # Parse command line arguments
    username, password, db_name = sys.argv[1:]

    # Create a connection to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
       )

    # Create the table(s) associated with the defined classes
    Base.metadata.create_all(engine)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
        # print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
