import requests
import sqlite3
from concurrent.futures import ThreadPoolExecutor
import json

API_URL = "http://localhost:8000/search"
DB_FILE = "test_results.db"
QUERY_FILE = "test_queries.txt"

# Make sure the DB and table exist BEFORE threading starts
def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY,
            query TEXT,
            summary TEXT,
            projects TEXT
        )
    """)
    conn.commit()
    conn.close()

setup_db()

with open(QUERY_FILE, "r") as f:
    queries = [line.strip() for line in f.readlines()]

def run_test(query):
    try:
        # Create new DB connection inside the thread
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()

        # Make API request
        response = requests.post(API_URL, json={"question": query})
        data = response.json()

        # Save result
        summary = data.get("summary", "")
        projects = json.dumps(data.get("projects", []))
        cur.execute("INSERT INTO test_results (query, summary, projects) VALUES (?, ?, ?)", (query, summary, projects))
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Error for query '{query}': {e}")

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(run_test, queries)

print("✅ Test completed. Results saved to SQLite.")
