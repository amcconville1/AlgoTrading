import os
from datetime import datetime
from data_fetcher import DataFetcher
from data_cleaner import clean_all_stock_files

if __name__ == "__main__":
    
    # Initialize DataFetcher and DataCleaner
    fetcher = DataFetcher()
    
    # Define paths for ticker files
    stock_ticker_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'stock_ticker.txt'))
    crypto_ticker_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'crypto_ticker.txt'))

    # Define date range for stocks
    start_date = '2024-01-01'
    end_date = '2024-09-14'

    # Ensure start_date is before end_date
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    if start_date_obj >= end_date_obj:
        raise ValueError("Start_date must be before end_date.")

    # Fetch stock data
    print("Fetching stock data...")
    fetcher.fetch_stock_data(stock_ticker_file, start_date, end_date)

    # Fetch crypto data
    print("Fetching crypto data...")
    fetcher.fetch_crypto_data(crypto_ticker_file)

    # Clean all stock files in the data/stocks directory
    clean_all_stock_files(data_dir='data/stocks', cleaned_data_dir='data/cleaned_stocks')