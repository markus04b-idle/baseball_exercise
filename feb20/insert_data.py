from sqlmodel import Session
from models import Faculty, engine

f1 = faculty_1 = Faculty(first_name="Christopher", last_name = "Mansour")


with Session(engine) as session:
    session.add(f1)
    session.commit()

