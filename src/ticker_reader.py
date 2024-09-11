class TickerReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_tickers(self):
        with open(self.file_path, 'r') as file:
            tickers = file.read().splitlines()
        return tickers