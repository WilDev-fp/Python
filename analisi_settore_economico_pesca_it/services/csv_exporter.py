import os

class CsvExporter:
    def __init__(self, output_folder='../static/output'):
        self.output_folder = output_folder
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def export(self, dataframe, filename):
        """
        Esporta il DataFrame come CSV nella cartella output,
        sovrascrivendo il file se esiste già.
        """
        output_path = os.path.join(self.output_folder, filename)
        # Se vuoi, elimina il file prima di salvare (non strettamente necessario)
        #if os.path.exists(output_path):
        #    os.remove(output_path)
        dataframe.to_csv(output_path, index=False)
        print(f"Esportato: {output_path}")
