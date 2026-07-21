from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

#Help wire FastAPI app to postgres

#pipe to database
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#parent class base for sql alchemy models to inherit from
Base = declarative_base()

#create a db session for transactions
#cache loaded objects for ORM state
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()