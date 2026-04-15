from fastapi import FastAPI, Query, HTTPException
import sqlite3
import os

app = FastAPI()

# ✅ Fix 1: Read secret from environment variable, never hardcode
API_KEY = os.environ.get("API_KEY")

# ✅ Fix 2: Secure DB connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()


@app.get("/")
def home():
    return {"message": "DevSecOps Demo App Running"}


# ✅ Fix 3: Parameterized query — no SQL injection possible
@app.get("/user")
def get_user(name: str = Query(...)):
    result = cursor.execute(
        "SELECT * FROM users WHERE name = ?", (name,)
    ).fetchall()
    return {"data": result}


# ✅ Fix 4: Debug endpoint removed — never expose secrets via API
# /debug endpoint deleted entirely
