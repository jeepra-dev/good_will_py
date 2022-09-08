from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, select
from database.Database import create_db_and_tables, engine

from models.Territories import Territories
from models.Territory_parents import Territory_parents

# db
create_db_and_tables()

# une session
session = Session()

def get_territory_by_id(id: int):
    with Session(engine) as session:
        statement = select(Territories).where(Territories.id == id)
        hero = session.exec(statement).one()
        print(hero)

def get_child_of_territory(id):
    # get child of territory
    subquery = session.query(Apartments.id).filter(Apartments.postcode == 2000).subquery()
    query = session.query(Residents).filter(Residents.apartment_id.in_(subquery))

    with Session(engine) as session:
        statement = select(Territory_parents.child_id)\
            .join(Territories, Territory_parents.parent_id == Territories.id)\
            .where(Territories.id == id)
        print(str(statement))
        hero = session.exec(statement).all()
        print(hero)

if __name__ == "__main__":
    #print(f"(get_territory_by_id:   {get_territory_by_id(100)})")
    print(f"(get_child_of_territory:   {get_child_of_territory(22)})")
