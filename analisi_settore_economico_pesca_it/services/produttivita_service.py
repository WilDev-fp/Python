import pandas as pd
import sqlite3

class ProduttivitaService:
    def __init__(self, db_path='../data/pesca.db'):
        self.conn = sqlite3.connect(db_path)

    def produttivita_per_area_anno(self):
        df_prod = pd.read_sql_query("SELECT * FROM produttivita", self.conn)
        df_reg = pd.read_sql_query("SELECT * FROM regioni", self.conn)
        df_prod = df_prod.merge(df_reg, left_on='regione', right_on='id_regione')
        return df_prod.groupby(['anno', 'area'])['produttivita_in_migliaia_euro'].sum().reset_index()

    def produttivita_nazionale_anno(self):
        df_prod = pd.read_sql_query("SELECT * FROM produttivita", self.conn)
        return df_prod.groupby('anno')['produttivita_in_migliaia_euro'].sum().reset_index()
