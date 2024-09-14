import os
import yfinance as yf
import pandas as pd
import ccxt
from ticker_reader import TickerReader

class DataFetcher:
    def __init__(self, data_dir='data/'):
        self.data_dir = data_dir
        os.makedirs(os.path.join(self.data_dir, 'stocks'), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, 'crypto'), exist_ok=True)

    def fetch_stock_data(self, ticker_file, start_date, end_date):
        # Read tickers from the file
        stock_tickers = TickerReader(ticker_file).read_tickers()

        # Fetch stock data for each symbol
        for stock_symbol in stock_tickers:
            try:
                print(f"Fetching stock data for {stock_symbol} from {start_date} to {end_date}")
                stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
                if stock_data.empty:
                    print(f"No data found for {stock_symbol}. Skipping.")
                else:
                    self.save_data(stock_data, stock_symbol, data_type='stock')
            except Exception as e:
                print(f"Failed to download stock data for {stock_symbol}: {e}")

    def fetch_crypto_data(self, ticker_file):
        # Read tickers from the file
        crypto_tickers = TickerReader(ticker_file).read_tickers()

        # Fetch crypto data for each symbol
        for crypto_symbol in crypto_tickers:
            try:
                exchange = ccxt.binance()  # You can change this to another exchange if needed
                since = exchange.parse8601('2018-01-01T00:00:00Z')
                print(f"Fetching crypto data for {crypto_symbol}")
                ohlcv = exchange.fetch_ohlcv(crypto_symbol, timeframe='1d', since=since)
                if not ohlcv:
                    print(f"No data found for {crypto_symbol}. Skipping.")
                else:
                    crypto_data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                    crypto_data['timestamp'] = pd.to_datetime(crypto_data['timestamp'], unit='ms')
                    self.save_data(crypto_data, crypto_symbol, data_type='crypto')
            except Exception as e:
                print(f"Failed to download crypto data for {crypto_symbol}: {e}")

    def save_data(self, data, symbol, data_type='stock'):
        folder = 'crypto' if data_type == 'crypto' else 'stocks'
        file_path = os.path.join(self.data_dir, folder, f'{symbol.replace("/", "_")}.csv')
        data.to_csv(file_path, index=False)
        print(f"Saved data for {symbol} to {file_path}")
