from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.storage.models import Base

# Create the engine with a hardcoded SQLite database path
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Initializes the database by creating all tables.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Returns a new database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
