from ticker_reader import TickerReader
from data_fetcher import StockDataFetcher

class DataManager:
    def __init__(self, ticker_file, start_date, end_date, data_dir='data/raw/'):
        self.ticker_reader = TickerReader(ticker_file)
        self.data_fetcher = StockDataFetcher(start_date, end_date, data_dir)

    def fetch_and_save_all_data(self):
        tickers = self.ticker_reader.read_tickers()
        for symbol in tickers:
            data = self.data_fetcher.fetch_data(symbol)
            self.data_fetcher.save_data(data, symbol)