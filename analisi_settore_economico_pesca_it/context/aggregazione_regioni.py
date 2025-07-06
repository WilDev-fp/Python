import sqlite3

class RegionTableManager:
    def __init__(self, db_path = "./data/pesca.db"):
        self.db_path = db_path        

    def insert_regions(self, region_list):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS regioni (
                    id_regione INTEGER PRIMARY KEY,
                    nome_regione TEXT,
                    area TEXT
                )
            """)
            conn.commit()
        """
        Inserisce una lista di tuple (id_regione, nome_regione, area) nella tabella.
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.executemany(
                "INSERT OR REPLACE INTO regioni (id_regione, nome_regione, area) VALUES (?, ?, ?)",
                region_list
            )
            conn.commit()

    def get_all(self):
        """
        Restituisce una lista di tutte le regioni nella tabella.
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id_regione, nome_regione, area FROM regioni ORDER BY id_regione")
            return cur.fetchall()

    def get_mapping(self):
        """
        Restituisce un dizionario: id_regione -> (nome_regione, area)
        """
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id_regione, nome_regione, area FROM regioni")
            return {row[0]: (row[1], row[2]) for row in cur.fetchall()}
