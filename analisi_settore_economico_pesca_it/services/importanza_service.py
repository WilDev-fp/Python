import pandas as pd
import sqlite3

class ImportanzaService:
    def __init__(self, db_path='../data/pesca.db'):
        self.db_path = db_path

    def media_perc_valore_aggiunto_per_area_anno(self):
        with sqlite3.connect(self.db_path) as conn:
            df_imp = pd.read_sql_query("SELECT * FROM importanza", conn)
            df_reg = pd.read_sql_query("SELECT * FROM regioni", conn)
            df_imp = df_imp.merge(df_reg, left_on='regione', right_on='id_regione')
            return df_imp.groupby(['anno', 'area'])['perc_valore_servizi'].mean().reset_index()
