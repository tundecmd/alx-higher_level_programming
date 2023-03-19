#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check that the script is being called correctly
    if (len(sys.argv) != 4):
        print("Usage: {} username password db_name".format(
            sys.argv[0]
            ))
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

    # Create a session object
    session = Session()

    # Query for the state with id = 2
    state = session.query(State).\
        filter(State.id == 2).first()

    # Update the name of the state
    state.name = "New Mexico"

    # Commit the session to the database
    session.commit()

    # Query for the state with id = 2
    states = session.query(State).order_by(State.id)

    # Display the results
    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Not found")

    # Close the session
    session.close()
