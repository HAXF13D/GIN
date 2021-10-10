import pandas as pd


class Csv_file:
    def __init__(self, filename):
        self.filename = filename

    def read_columns(self):
        data = pd.read_csv(self.filename)
        return data.columns.values
