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
    companies = {}
    try:
        with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)

            count = 0
            for row in csv_reader:
                # Handle BOM in column names
                clean_row = {key.lstrip(
                    '\ufeff'): value for key, value in row.items()}

                company_name = clean_row.get('cname')
                if company_name in companies:
                    company = companies[company_name]
                else:
                    company = models.Company(name=company_name)
                    db.add(company)
                    db.commit()
                    db.refresh(company)
                companies[company_name] = company

                try:
                    pname = clean_row.get('pname')
                    if not pname:
                        print(
                            f"Skipping row {count + 1}: Missing product name")
                        print(clean_row)
                        continue

                    drug = models.Drug(
                        product_name=pname,
                        effect=clean_row.get('effect') or None,
                        dosage=clean_row.get('dosage') or None,
                        dprecaution=clean_row.get('dprecaution') or None,
                        interaction=clean_row.get('interaction') or None,
                        side_effect=clean_row.get('side_effect') or None,
                        storage=clean_row.get('storage') or None,
                        company_id=company.id,
                        lang_id=2
                    )

                    db.add(drug)
                    count += 1
                except Exception as e:
                    print(f"Error processing row {count + 1}: {e}")
                    print("Row data:", clean_row)
                    continue

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
    csv_file = "translated_en_drug_data_full.csv"  # Adjust path as needed

    if not Path(csv_file).exists():
        print(f"Error: CSV file '{csv_file}' not found!")
        sys.exit(1)

    print(f"Starting import from {csv_file}...")
    import_drug_data(csv_file)


if __name__ == "__main__":
    main()
