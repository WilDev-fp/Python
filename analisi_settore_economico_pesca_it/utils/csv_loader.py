import pandas as pd

class CsvLoader:
    def __init__(self, filepath, sep=None, encoding=None):
        self.filepath = filepath
        self.sep = sep
        self.encoding = encoding
        self.df = None

    def load(self):
        try:
            df = pd.read_csv(self.filepath, sep=self.sep, encoding=self.encoding)
        except UnicodeDecodeError:
            df = pd.read_csv(self.filepath, sep=self.sep, encoding='latin1')
        return df