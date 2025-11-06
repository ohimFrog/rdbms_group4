"""
Seed script to populate initial/sample data into the database.

Usage:
    python -m scripts.seed_data
"""
from database import SessionLocal, init_db
import models


def seed_languages():
    """Seed initial language data."""
    db = SessionLocal()
    try:
        languages = [
            {"code": "ko", "name": "Korean"},
            {"code": "en-US", "name": "English USA"},
            # {"code": "ja", "name": "Japanese"},
        ]

        for lang_data in languages:
            existing = db.query(models.Lang).filter_by(
                code=lang_data["code"]).first()
            if not existing:
                lang = models.Lang(**lang_data)
                db.add(lang)

        db.commit()
        print(f"Seeded {len(languages)} languages")
    except Exception as e:
        db.rollback()
        print(f"Error seeding languages: {e}")
        raise
    finally:
        db.close()


def main():
    """Main entry point for seeding data."""
    print("Initializing database...")
    init_db()

    print("Seeding data...")
    seed_languages()

    print("Seeding complete!")


if __name__ == "__main__":
    main()
