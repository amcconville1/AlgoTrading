from data_fetcher import DataFetcher

def test_stock_data():
    data_fetcher = DataFetcher()
    stock_symbol = 'MSFT'
    start_date = '2018-01-01'
    end_date = '2018-01-05'
    stock_data = data_fetcher.fetch_stock_data(stock_symbol, start_date, end_date)
    if stock_data is not None:
        data_fetcher.save_data(stock_data, stock_symbol, data_type='stock')

def test_crypto_data():
    data_fetcher = DataFetcher()
    crypto_symbol = 'BTC/USDT'
    crypto_data = data_fetcher.fetch_crypto_data(crypto_symbol)
    if crypto_data is not None:
        data_fetcher.save_data(crypto_data, crypto_symbol, data_type='crypto')


if __name__ == "__main__":
    stock_symbol = input("Stock:")
    test_crypto_data()
    test_stock_data()