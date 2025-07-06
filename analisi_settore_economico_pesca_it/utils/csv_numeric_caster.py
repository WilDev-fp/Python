import pandas as pd

class CsvNumericCaster:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def to_numeric(self, columns):
        for col in columns:
            # Solo per colonne oggetto (stringa)
            if self.df[col].dtype == 'O':
                self.df[col] = self.df[col].str.replace(',', '.', regex=False).replace(['', 'nan', 'None', None], pd.NA)

            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        return self.get()

    def get(self):
        return self.df
