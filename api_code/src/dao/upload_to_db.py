import pandas as pd
import sqlite3
import os


def load_data_to_db(db_file, df):
    """
    Loads investor and commitment data from a DataFrame into an SQLite database.
    """
    inv_cache = {}

    try:
        
        with open(db_file, 'ab'):
            pass  

        with sqlite3.connect(db_file) as conn:
            c = conn.cursor()
            for _, row in df.iterrows():
                key = (
                    row['Investor Name'],
                    row['Investory Type'],
                    row['Investor Country'],
                    row['Investor Date Added']
                )
                if key not in inv_cache:
                    c.execute("""
                        INSERT INTO investors (name, type, country, date_added, last_updated)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        row['Investor Name'],
                        row['Investory Type'],
                        row['Investor Country'],
                        row['Investor Date Added'],
                        row['Investor Last Updated']
                    ))
                    inv_cache[key] = c.lastrowid
                investor_id = inv_cache[key]
                c.execute("""
                    INSERT INTO commitments (investor_id, asset_class, amount, currency)
                    VALUES (?, ?, ?, ?)
                """, (
                    investor_id,
                    row['Commitment Asset Class'],
                    row['Commitment Amount'],
                    row['Commitment Currency']
                ))
            conn.commit()
        print("Data processed and loaded into the database successfully.")

    except Exception as e:
        print(f"Database operation failed: {e}")


if __name__ == "__main__":
    csv_file = 'api_code/src/input/fund_acct.csv'
    db_file = '/Users/bishnudas/asset_funds.db'

    try:
        df = pd.read_csv(csv_file)
        load_data_to_db(db_file, df)
        print("Test succeeded.")
    except Exception as e:
        print(f"Error during test: {e}")




