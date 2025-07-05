
from fastapi import FastAPI

import sqlite3
import pandas as pd

app = FastAPI()

DB_PATH = "C:/Users/utente/Desktop/prj-python/Python/data/db/report.db"

@app.get("/dati")
async def get_dati():
    # Connessione a SQLite
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM amianto LIMIT 10"
    df = pd.read_sql_query(query, conn)
    conn.close()
    # Converti in dizionario per risposta JSON
    return df.to_dict(orient="records")


    
