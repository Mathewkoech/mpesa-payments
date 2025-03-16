import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from databases import Database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the values from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")
MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE")
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")
MPESA_PASSWORD = os.getenv("MPESA_PASSWORD")
MPESA_ENV = os.getenv("MPESA_ENV")

# Set up the database connection
database = Database(DATABASE_URL)

# SQLAlchemy for database operations
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
