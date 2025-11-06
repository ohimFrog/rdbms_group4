"""
Utility script to clear/reset database data.

Usage:
    python -m scripts.reset_database
"""
from database import SessionLocal, engine, Base, init_db
import models


def reset_database():
    """Drop all tables and recreate them."""
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)

    print("Creating tables...")
    init_db()

    print("Database reset complete!")


def clear_all_data():
    """Clear all data from tables without dropping them."""
    db = SessionLocal()
    try:
        print("Clearing all data...")
        db.query(models.Feedback).delete()
        db.query(models.Drug).delete()
        db.query(models.Company).delete()
        db.query(models.Lang).delete()
        db.query(models.User).delete()
        db.commit()
        print("All data cleared!")
    except Exception as e:
        db.rollback()
        print(f"Error clearing data: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--clear-only":
        clear_all_data()
    else:
        reset_database()
