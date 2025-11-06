from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create engine for MySQL
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,          # Test connections before using them
    pool_recycle=3600,            # Recycle connections after 1 hour
    pool_size=5,                  # Number of connections to maintain
    max_overflow=10,              # Max connections beyond pool_size
    connect_args={
        "connect_timeout": 10,    # Connection timeout in seconds
    },
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize the database by creating all tables"""
    try:
        # Import models here to ensure they're registered with Base
        import models

        # Test the connection first
        with engine.connect() as connection:
            print("Database connection successful!")

        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("Tables created:", list(Base.metadata.tables.keys()))

    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
