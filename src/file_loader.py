from pathlib import Path

import pandas as pd

class FileLoader:
    def __init__(self, filepath, sep=None, encoding=None):
        self.filepath = filepath
        self.sep = sep
        self.encoding = encoding
        self.df = None

    def load(self):
        # Crea il dizionario KeyWordsArguments dei parametri opzionali
        kwargs = {}
        if self.sep is not None:
            kwargs['sep'] = self.sep
        if self.encoding is not None:
            kwargs['encoding'] = self.encoding
        
        try:
            self.df = pd.read_csv(self.filepath, **kwargs)
        except FileNotFoundError:
            print(f"Errore: File non trovato in {self.filepath}")
            raise

        return self.df