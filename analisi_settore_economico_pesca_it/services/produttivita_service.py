import pandas as pd
import sqlite3

class ProduttivitaService:
    def __init__(self, db_path='../data/pesca.db'):
        self.db_path = db_path

    def produttivita_per_area_anno(self):
        with sqlite3.connect(self.db_path) as conn:
            df_prod = pd.read_sql_query("SELECT * FROM produttivita", conn)
            df_reg = pd.read_sql_query("SELECT * FROM regioni", conn)
            df_prod = df_prod.merge(df_reg, left_on='regione', right_on='id_regione')
            return df_prod.groupby(['anno', 'area'])['produttivita_in_migliaia_euro'].sum().reset_index()

    def produttivita_nazionale_anno(self):
        with sqlite3.connect(self.db_path) as conn:
            df_prod = pd.read_sql_query("SELECT * FROM produttivita", conn)
            return df_prod.groupby('anno')['produttivita_in_migliaia_euro'].sum().reset_index()
