import yfinance as yf
import pandas as pd
import os
import ccxt


class DataFetcher:
    def __init__(self, data_dir='data/'):
        self.data_dir = data_dir
        os.makedirs(os.path.join(self.data_dir, 'raw'), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, 'crypto'), exist_ok=True)

    def fetch_stock_data(self, symbol, start_date, end_date):
        try:
            data = yf.download(symbol, start=start_date, end=end_date)
            if data.empty:
                print(f"No data found for {symbol}. Skipping.")
                return None
            return data
        except Exception as e:
            print(f"Failed to download data for {symbol}: {e}")
            return None

    def fetch_crypto_data(self, symbol, exchange_id='cryptocom', timeframe='1d', since=None, limit=1000):
        try:
            exchange = getattr(ccxt, exchange_id)()
            if timeframe is None:
                timeframe = '1d'
            if since is None:
                since = exchange.parse8601('2018-01-01T00:00:00Z')
            print(f"Fetching crypto data for {symbol} from {since} with timeframe {timeframe}")
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            if not ohlcv:
                print(f"No data found for {symbol}. Skipping.")
                return None
            data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
            return data
        except Exception as e:
            print(f"Failed to download data for {symbol}: {e}")
            return None
    
    def save_data(self, data, symbol, data_type='stock'):
        folder = 'crypto' if data_type == 'crypto' else 'raw'
        file_path = os.path.join(self.data_dir, folder, f'{symbol.replace("/", "_")}.csv')
        data.to_csv(file_path, index=False)
        print(f'Saved data for {symbol} to {file_path}')