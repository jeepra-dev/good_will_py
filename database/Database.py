from sqlmodel import SQLModel, create_engine

sqlite_url = "mysql+mysqldb://toto:toto@localhost/good_will"
engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)