import pandas as pd

class AmiantoCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def _rename_columns(self):
        self.df = self.df.rename(columns={
            'Comune': 'comune',
            'tipo_attività': 'tipo_attivita',
            'sensibilità_misura': 'sensibilita_misura'
        })

    """
    Converte la colonna indicata del DataFrame in formato datetime.

    - Si aspetta che i valori in input siano stringhe in formato europeo: 'GG/MM/AAAA' (es: '30/01/2024').
    - Se trova una data non valida, vuota o in formato non riconosciuto, la sostituisce con NaT (valore mancante per pandas).
    - L'output della colonna sarà di tipo datetime64[ns] e verrà visualizzato in formato ISO 'YYYY-MM-DD' (es: '2024-01-30').
    - Esempi:
        - '15/02/2024' -> 2024-02-15
        - '31/04/2022' -> NaT   (data non esistente)
        - 'abc'        -> NaT   (valore non valido)
        - ''           -> NaT   (vuoto)
    """
    def _to_datetime(self, column):
        self.df[column] = pd.to_datetime(self.df[column], dayfirst=True, errors='coerce')

    def _to_float(self, columns):
        for col in columns:
            self.df[col] = (
                self.df[col]
                .astype(str)
                .str.replace(',', '.')
                .replace(['', 'nan', 'None', None], pd.NA)
                
            )
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    """
    Riempi i valori mancanti (NaN) nelle colonne specificate con il valore dato.

    Args:
        columns (list): lista delle colonne su cui applicare il riempimento.
        value (str, opzionale): valore con cui riempire i NaN (default 'N.A.')
    """
    def _fillna_values(self, columns, value='N.A.'):
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna(value)

    def _standardize_strings(self, columns):
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.lower().str.strip()


    """
    Elimina tutte le righe che contengono almeno un valore mancante (NaN)
    nelle colonne specificate.

    Args:
        columns (str o list): Nome della colonna o lista di colonne su cui fare il controllo.

    Esempi:
        self._drop_empty_rows('concentrazione')
        self._drop_empty_rows(['concentrazione', 'impianto'])
    """
    def _drop_empty_rows(self, columns):
        # Metodo per una sola colonna
        #self.df = self.df[self.df[column].notna()]

        if isinstance(columns, str):
            columns = [columns]
        self.df = self.df.dropna(subset=columns)


    """
    Aggiorna il DataFrame senza le righe che hanno almeno un valore mancante
    nelle colonne specificate.
    
    Args:
        df (pd.DataFrame): Il DataFrame da pulire.
        columns (list): Lista di colonne da controllare.
    """
    def _drop_rows_with_missing(self, columns):
        self.df = self.df.dropna(subset=columns)

    # Tutti i passaggi di pulizia in sequenza
    def get_cleaned(self):
        self._rename_columns()
        self._to_datetime('data_campionamento')
        self._to_float(['limite_normativo', 'concentrazione'])
        self._fillna_values(['impianto', 'presenza_di_fibre'])
        self._standardize_strings(['presenza_di_fibre', 'comune', 'esito_normativo'])
        self._drop_empty_rows('concentrazione')
        return self.df
