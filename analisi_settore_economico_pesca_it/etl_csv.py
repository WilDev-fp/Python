import time

from utils.csv_loader import CsvLoader
from utils.csv_renamer import CsvRenamer
from utils.csv_numeric_caster import CsvNumericCaster
from utils.csv_transformer import CsvTransformer
from services.csv_exporter import CsvExporter
from context.sqlite_uploader import SqliteUploader
from context.aggregazione_regioni import RegionTableManager

csv_path_andamento = "./static/Andamento occupazione del settore della pesca per regione_0.csv"
csv_path_importanza = "./static/Importanza economica del settore della pesca per regione.csv"
csv_path_produttivita = "./static/Produttività del settore della pesca per regione.csv"

exporter = CsvExporter(output_folder="./static/output")

# ETL Andamento
try:
    # encoding='latin1'  → Vecchi file Windows/Europa occidentale
    # encoding='cp1252'  → Variante Windows, gestisce più simboli (€ ecc.)
    # encoding='utf-8-sig' → Da usare se la prima colonna ha caratteri strani (BOM UTF-8), tipico da Excel
    # Provare diversi encoding se si vedono caratteri strani nei dati/colonne!
    loader = CsvLoader(csv_path_andamento,';','utf-8-sig')
    df_Andamento = loader.load()
    print("Dati caricati correttamente:")
except Exception as e:
    print(f"Errore nel caricamento: {e}")
    raise

columns_map = {
    'Anno': 'anno',
    'Regione': 'regione',
    'Variazione percentuale  unità di lavoro della pesca': 'variazione_perc_occupazione'
}

renamer = CsvRenamer(df_Andamento)
df_andamento_rinominato = renamer.rename_columns(columns_map)

num_cols = ['anno', 'regione', 'variazione_perc_occupazione']
caster = CsvNumericCaster(df_andamento_rinominato)
df_andamento_numeric_casted = caster.to_numeric(num_cols)

cleaner = CsvTransformer(df_andamento_numeric_casted)
df_andamento_normalized = cleaner.get_cleaned()

# Caricamento dati
#SqliteUploader().upload_dataframe(df_andamento_normalized, 'andamento')
exporter.export(df_andamento_normalized, 'andamento_clean.csv')
time.sleep(1)
SqliteUploader().upload_csv('./static/output/andamento_clean.csv', 'andamento')


# ETL Importanza
try:
    # encoding='latin1'  → Vecchi file Windows/Europa occidentale
    # encoding='cp1252'  → Variante Windows, gestisce più simboli (€ ecc.)
    # encoding='utf-8-sig' → Da usare se la prima colonna ha caratteri strani (BOM UTF-8), tipico da Excel
    # Provare diversi encoding se si vedono caratteri strani nei dati/colonne!
    loader = CsvLoader(csv_path_importanza,';','utf-8-sig')
    df_Importanza = loader.load()
    print("Dati caricati correttamente:")
except Exception as e:
    print(f"Errore nel caricamento: {e}")
    raise

columns_map = {
    'Anno': 'anno',
    'Regione': 'regione',
    'Percentuale valore aggiunto pesca-piscicoltura-servizi': 'perc_valore_servizi'
}

renamer = CsvRenamer(df_Importanza)
df_importanza_rinominato = renamer.rename_columns(columns_map)

num_cols = ['anno', 'regione', 'perc_valore_servizi']
caster = CsvNumericCaster(df_importanza_rinominato)
df_importanza_numeric_casted = caster.to_numeric(num_cols)

cleaner = CsvTransformer(df_importanza_numeric_casted)
df_importanza_normalized = cleaner.get_cleaned()

# Caricamento dati
#SqliteUploader().upload_dataframe(df_importanza_normalized, 'importanza')
exporter.export(df_importanza_normalized, 'importanza_clean.csv')
time.sleep(1)
SqliteUploader().upload_csv('./static/output/importanza_clean.csv', 'importanza')


# ETL Produttività
try:
    # encoding='latin1'  → Vecchi file Windows/Europa occidentale
    # encoding='cp1252'  → Variante Windows, gestisce più simboli (€ ecc.)
    # encoding='utf-8-sig' → Da usare se la prima colonna ha caratteri strani (BOM UTF-8), tipico da Excel
    # Provare diversi encoding se si vedono caratteri strani nei dati/colonne!
    loader = CsvLoader(csv_path_produttivita,';','utf-8-sig')
    df_Produttivita = loader.load()
    print("Dati caricati correttamente:")
except Exception as e:
    print(f"Errore nel caricamento: {e}")
    raise

columns_map = {
    'Anno': 'anno',
    'Regione': 'regione',
    'Produttivit� in migliaia di euro': 'produttivita_in_migliaia_euro'
}

renamer = CsvRenamer(df_Produttivita)
df_produttivita_rinominato = renamer.rename_columns(columns_map)

num_cols = ['anno', 'regione', 'produttivita_in_migliaia_euro']
caster = CsvNumericCaster(df_produttivita_rinominato)
df_produttivita_numeric_casted = caster.to_numeric(num_cols)

cleaner = CsvTransformer(df_produttivita_numeric_casted)
df_produttivita_normalized = cleaner.get_cleaned()

# Caricamento dati
SqliteUploader().upload_dataframe(df_produttivita_normalized, 'produttivita')
exporter.export(df_produttivita_normalized, 'produttivita_clean.csv')

# Creazione tabella regioni
mapping_regioni = [
    (1, "Piemonte", "Nord-ovest"),
    (2, "Valle d'Aosta", "Nord-ovest"),
    (3, "Lombardia", "Nord-ovest"),
    (4, "Liguria", "Nord-ovest"),
    (5, "Trentino-Alto Adige", "Nord-est"),
    (6, "Veneto", "Nord-est"),
    (7, "Friuli-Venezia Giulia", "Nord-est"),
    (8, "Emilia-Romagna", "Nord-est"),
    (9, "Toscana", "Centro"),
    (10, "Umbria", "Centro"),
    (11, "Marche", "Centro"),
    (12, "Lazio", "Centro"),
    (13, "Abruzzo", "Centro"),
    (14, "Molise", "Sud"),
    (15, "Campania", "Sud"),
    (16, "Puglia", "Sud"),
    (17, "Basilicata", "Sud"),
    (18, "Calabria", "Sud"),
    (19, "Sicilia", "Isole"),
    (20, "Sardegna", "Isole")
]

regioni = RegionTableManager()
regioni.insert_regions(mapping_regioni)

print(regioni.get_all())