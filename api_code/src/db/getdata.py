import sqlite3

def get_investor_commitments(db_file):
    data = []

    try:
        with sqlite3.connect(db_file) as conn:
            c = conn.cursor()
            c.execute("""
                SELECT
                    i.name, i.type, i.country, i.date_added, i.last_updated,
                    c.asset_class, c.amount, c.currency
                FROM investors i
                LEFT JOIN commitments c ON i.id = c.investor_id
            """)
            rows = c.fetchall()
            for row in rows:
                data.append({
                    "name": row[0],
                    "type": row[1],
                    "country": row[2],
                    "date_added": row[3],
                    "last_updated": row[4],
                    "asset_class": row[5],
                    "amount": row[6],
                    "currency": row[7]
                })
        return data

    except Exception as e:
        print(f"Database read failed: {e}")
        return []

if __name__ == "__main__":
    path = '/Users/bishnudas/asset_funds.db'
    print("data:::", get_investor_commitments(path))
