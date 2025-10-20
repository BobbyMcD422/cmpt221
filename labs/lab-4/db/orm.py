"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: create three professor objects *DONE*
        professor1 = Professor(FirstName="Donald", LastName="Schwartz", Email="donald.schwartz@marist.edu")
        professor2 = Professor(FirstName="Calista", LastName="Phippen", Email="calista.phippen1@marist.edu")
        professor3 = Professor(FirstName="Red", LastName="Fox", Email="red.fox@marist.edu")
        
        # TODO: use the sqlalchemy orm to insert the new records as a list of professor objects *DONE*
        session.add_all([professor1, professor2, professor3])
        # "save" the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be updated (would ideally be a parameter) *DONE*
        professor = session.query(Professor).filter(Professor.ProfessorID == 13).first()

        # TODO: use the sqlalchemy orm to update 1 record *DONE*
        if professor:
            professor.FirstName = "John"
            professor.Email = "john@marist.edu"
            # "save" the changes
            session.commit()
        else:
            print(f"No Prof with that ID :/")

    
    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)
        
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be deleted (would ideally be a parameter) *DONE*
        professor = session.query(Professor).filter(Professor.ProfessorID == 14).first()

        # TODO: use the sqlalchemy orm to delete 1 record
        if professor:
            session.delete(professor)
            # "save" the changes
            session.commit()
        else:
            print(f"No Prof found :/ to delete")

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()

