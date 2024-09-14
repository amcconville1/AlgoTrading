from ticker_reader import TickerReader
from data_fetcher import DataFetcher

class DataManager:
    def __init__(self, ticker_file, start_date, end_date, data_dir='data/'):
        self.ticker_reader = TickerReader(ticker_file)
        self.data_fetcher = DataFetcher(data_dir)  # Initialize DataFetcher instance
        self.start_date = start_date
        self.end_date = end_date

    def fetch_and_save_all_data(self):
        tickers = self.ticker_reader.read_tickers()
        for symbol in tickers:
            # Fetch stock data for each symbol using the start and end date
            data = self.data_fetcher.fetch_stock_data(symbol, self.start_date, self.end_date)
            if data is not None:
                # Save the fetched data
                self.data_fetcher.save_data(data, symbol, data_type='stock')
