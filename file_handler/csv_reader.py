from file_handler.file_reader import FileReader
import pandas as pd

class CsvReader(FileReader):
    def __init__(self,address,name):
        super(CsvReader, self).__init__(address,name)

    def read_data(self):
        return pd.read_csv(self.address)


