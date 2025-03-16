from databases import Database
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Async database connection
database = Database(DATABASE_URL)
metadata = MetaData()

# SQLAlchemy Base class
Base = declarative_base(metadata=metadata)

# Synchronous session maker
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
