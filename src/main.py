import sys
import os
from datetime import datetime
from data_fetcher import CryptoDataFetcher

# Add the src directory to the system path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.append(src_path)
# print(sys.path) # Prints sys.path to debug


from data_manager import StockDataFetcher

if __name__ == "__main__":
    ticker_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tickers.txt'))
    start_date = '2018-01-01'
    end_date = '2018-01-05'

    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj =  datetime.strptime(end_date, '%Y-%m-%d')
    
    # Ensure start_date is before end_date
    if start_date_obj >= end_date_obj:
        raise ValueError("Start_date must be before end_date.")

    data_manager = StockDataFetcher(ticker_file, start_date, end_date)
    data_manager.fetch_and_save_all_data()

    # Crypto fetcher
    # Likely need to comment ou tthe top stock fetcher and uncomment below to grab crypto history.
    ### TODO NEED TO REFACTOR TO EXECUTE BOTH BASED ON WHAT?

    # fetcher = CryptoDataFetcher()
    # symbol = 'BTC/USDT' # Bitcoin to USDT
    # data = fetcher.fetch_data(symbol)
    # fetcher.save_data(data, symbol)
