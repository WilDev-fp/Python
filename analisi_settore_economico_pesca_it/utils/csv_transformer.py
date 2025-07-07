import pandas as pd

class CsvTransformer:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def _clean_missing(self):
        # Sostituisci valori mancanti tramite interpolazione numerica (per colonne numeriche)
        self.df = self.df.interpolate(method='linear', axis=0, limit_direction='both')

    def _drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    def get_cleaned(self):
        self._clean_missing()
        self._drop_duplicates()
        return self.df