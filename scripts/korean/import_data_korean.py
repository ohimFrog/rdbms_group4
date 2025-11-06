"""
Data import script for loading drug data from CSV into the database.

Usage:
    python -m scripts.import_data
    or
    python scripts/import_data.py
"""
import sys
import csv
from pathlib import Path
from database import SessionLocal, init_db
import models


def import_drug_data(csv_file_path: str):
    """
    Import drug data from CSV file into the database.

    Args:
        csv_file_path: Path to the CSV file containing drug data
    """
    init_db()

    db = SessionLocal()
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            count = 0
            for row in csv_reader:

                drug = models.Drug(
                    product_name=row.get('product_name'),
                    effect=row.get('effect'),
                    dosage=row.get('dosage'),
                    dprecaution=row.get('dprecaution'),
                    interaction=row.get('interaction'),
                    side_effect=row.get('side_effect'),
                    storage=row.get('storage'),
                    # Add lang_id and company_id handling here
                )

                db.add(drug)
                count += 1

                # Commit in batches to avoid large transactions
                if count % 100 == 0:
                    db.commit()
                    print(f"Imported {count} records...")

            db.commit()
            print(f"Successfully imported {count} records")

    except Exception as e:
        db.rollback()
        print(f"Error importing data: {e}")
        raise
    finally:
        db.close()


def main():
    """Main entry point for the import script."""
    csv_file = "drug_data_korean.csv"  # Adjust path as needed

    if not Path(csv_file).exists():
        print(f"Error: CSV file '{csv_file}' not found!")
        sys.exit(1)

    print(f"Starting import from {csv_file}...")
    import_drug_data(csv_file)


if __name__ == "__main__":
    main()
