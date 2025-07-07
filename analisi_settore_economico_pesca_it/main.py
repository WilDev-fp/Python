from fastapi import FastAPI, Query, HTTPException
from services.produttivita_service import ProduttivitaService
from services.importanza_service import ImportanzaService
from services.occupazione_service import OccupazioneService
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import sqlite3

app = FastAPI()

# Abilita CORS per tutti i domini (sviluppo locale, va bene!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # oppure ["http://127.0.0.1:5500"] per sicurezza
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inizializza i servizi (puoi anche metterli come dependency)
prod_service = ProduttivitaService(db_path='./data/pesca.db')
imp_service = ImportanzaService(db_path='./data/pesca.db')
occ_service = OccupazioneService(db_path='./data/pesca.db')

def filter_by_anno(df, da_anno: int = None, a_anno: int = None):
    if da_anno is not None:
        df = df[df['anno'] >= da_anno]
    if a_anno is not None:
        df = df[df['anno'] <= a_anno]
    return df

@app.get("/serie/produttivita_per_area")
def get_produttivita_per_area(da_anno: int = Query(None), a_anno: int = Query(None)):
    df = prod_service.produttivita_per_area_anno()
    if da_anno is not None or a_anno is not None:
        df = filter_by_anno(df, da_anno, a_anno)
    return df.to_dict(orient="records")

@app.get("/serie/produttivita_nazionale")
def get_produttivita_nazionale(da_anno: int = Query(None), a_anno: int = Query(None)):
    df = prod_service.produttivita_nazionale_anno()
    if da_anno is not None or a_anno is not None:
        df = filter_by_anno(df, da_anno, a_anno)
    return df.to_dict(orient="records")

@app.get("/serie/media_perc_valore_aggiunto")
def get_media_perc_valore_aggiunto(da_anno: int = Query(None), a_anno: int = Query(None)):
    df = imp_service.media_perc_valore_aggiunto_per_area_anno()
    if da_anno is not None or a_anno is not None:
        df = filter_by_anno(df, da_anno, a_anno)
    return df.to_dict(orient="records")

@app.get("/serie/media_var_occupazione_nazionale")
def get_media_var_occupazione_nazionale(da_anno: int = Query(None), a_anno: int = Query(None)):
    df = occ_service.media_var_occupazione_nazionale()
    if da_anno is not None or a_anno is not None:
        df = filter_by_anno(df, da_anno, a_anno)
    return df.to_dict(orient="records")

@app.get("/serie/media_var_occupazione_per_area")
def get_media_var_occupazione_per_area(da_anno: int = Query(None), a_anno: int = Query(None)):
    df = occ_service.media_var_occupazione_per_area_anno()
    if da_anno is not None or a_anno is not None:
        df = filter_by_anno(df, da_anno, a_anno)
    return df.to_dict(orient="records")

# Esportazione delle 3 tabelle di base
@app.get("/tabella/{nome_tabella}")
def get_tabella(nome_tabella: str, da_anno: int = Query(None), a_anno: int = Query(None)):
    allowed = ["andamento", "importanza", "produttivita"]
    if nome_tabella not in allowed:
        raise HTTPException(status_code=404, detail="Tabella non trovata")
    with sqlite3.connect('./data/pesca.db') as conn:
        df = pd.read_sql_query(f"SELECT * FROM {nome_tabella}", conn)
        if da_anno is not None or a_anno is not None:
            df = filter_by_anno(df, da_anno, a_anno)
        return df.to_dict(orient="records")
