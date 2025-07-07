import pandas as pd
import sqlite3

class OccupazioneService:
    def __init__(self, db_path='../data/pesca.db'):
        self.db_path = db_path

    def media_var_occupazione_nazionale(self):
        with sqlite3.connect(self.db_path) as conn:
            df_and = pd.read_sql_query("SELECT * FROM andamento", conn)
            return df_and.groupby('anno')['variazione_perc_occupazione'].mean().reset_index()

    def media_var_occupazione_per_area_anno(self):
        with sqlite3.connect(self.db_path) as conn:
            df_and = pd.read_sql_query("SELECT * FROM andamento", conn)
            df_reg = pd.read_sql_query("SELECT * FROM regioni", conn)
            df_and = df_and.merge(df_reg, left_on='regione', right_on='id_regione')
            return df_and.groupby(['anno', 'area'])['variazione_perc_occupazione'].mean().reset_index()
