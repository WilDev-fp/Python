import os
import sqlite3
import pandas as pd

class SqliteUploader:
    def __init__(self, db_path = "./data/pesca.db"):
        self.db_path = db_path
        # Crea la cartella se non esiste
        db_folder = os.path.dirname(self.db_path)
        if db_folder and not os.path.exists(db_folder):
            os.makedirs(db_folder)

    def upload_csv(self, csv_path, table_name):
        """
        Carica un file CSV in una tabella del database SQLite.
        :param csv_path: percorso file CSV
        :param table_name: nome tabella nel database
        """
        df = pd.read_csv(csv_path)
        self.upload_dataframe(df, table_name)

    def upload_dataframe(self, df, table_name):
        """
        Carica un DataFrame in una tabella del database SQLite.
        :param df: pandas DataFrame
        :param table_name: nome tabella nel database
        """
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"TABELLA '{table_name}' CARICATA con {len(df)} record.")

