class CsvRenamer:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def rename_columns(self, columns_map):
        """
        Rinominare le colonne secondo un dizionario.
        Esempio: {'VecchioNome': 'NuovoNome'}
        """
        self.df = self.df.rename(columns=columns_map)
        return self.get()

    def get(self):
        return self.df
