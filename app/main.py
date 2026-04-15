from fastapi import FastAPI, Query
import sqlite3

app = FastAPI()

# ❌ Hardcoded secret (for secret scanning demo)
API_KEY = "AWS_SECRET_ACCESS_KEY=1234567890abcdef"

# ❌ Insecure DB connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()


@app.get("/")
def home():
    return {"message": "DevSecOps Demo App Running"}


# ❌ SQL Injection vulnerability
@app.get("/user")
def get_user(name: str = Query(...)):
    query = f"SELECT * FROM users WHERE name = '{name}'"
    result = cursor.execute(query).fetchall()
    return {"data": result}


# ❌ Debug info exposure
@app.get("/debug")
def debug():
    return {"api_key": API_KEY}