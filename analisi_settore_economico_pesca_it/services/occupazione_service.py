import pandas as pd
import sqlite3

class OccupazioneService:
    def __init__(self, db_path='../data/pesca.db'):
        self.conn = sqlite3.connect(db_path)

    def media_var_occupazione_nazionale(self):
        df_and = pd.read_sql_query("SELECT * FROM andamento", self.conn)
        return df_and.groupby('anno')['variazione_perc_occupazione'].mean().reset_index()

    def media_var_occupazione_per_area_anno(self):
        df_and = pd.read_sql_query("SELECT * FROM andamento", self.conn)
        df_reg = pd.read_sql_query("SELECT * FROM regioni", self.conn)
        df_and = df_and.merge(df_reg, left_on='regione', right_on='id_regione')
        return df_and.groupby(['anno', 'area'])['variazione_perc_occupazione'].mean().reset_index()
