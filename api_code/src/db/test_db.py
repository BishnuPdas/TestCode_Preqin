from database import get_db 

def test_db_connection():
    
    db = next(get_db())
    try:  
        result = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = result.fetchall()
        print("Tables in DB:", tables)
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()
