import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Use DATABASE_URL from environment if present, otherwise a harmless local default.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://course_role:mypassword@localhost:5432/myappdb")
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user_name:mypassword@localhost:5432/dbname")


# Note: prefer setting the DATABASE_URL environment variable in production or
# when running the app locally. dotenv is loaded above so placing a `.env`
# file with DATABASE_URL=postgresql://course_role:... will override this default.

# Create SQLAlchemy engine and session factory
engine = create_engine(DATABASE_URL)

# Standard SessionLocal for dependency injection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Example DATABASE_URL formats:
# postgresql://username:password@host:port/dbname