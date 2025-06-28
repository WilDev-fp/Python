import pandas as pd
from pathlib import Path

# Percorso del file CSV (usa path relativo)
csv_path = Path("../Python/data/input/determinazioni_amianto_2024.csv")
# Leggi il CSV con pandas
try:
    df = pd.read_csv(csv_path, sep=';')
    print("Dati caricati correttamente:")
    print(df.head())
except FileNotFoundError:
    print(f"Errore: File non trovato in {csv_path}")