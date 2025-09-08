import sqlite3

db_file = 'asset_funds.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

#one time table creation

# Investors Table
c.execute("""
CREATE TABLE investors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    country TEXT,
    date_added TEXT,
    last_updated TEXT
)
""")

# Commitments Table
c.execute("""
CREATE TABLE commitments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id INTEGER,
    asset_class TEXT,
    amount REAL,
    currency TEXT,
    FOREIGN KEY (investor_id) REFERENCES investors(id)
)
""")

conn.commit()
conn.close()
print("Database and tables created successfully.")
