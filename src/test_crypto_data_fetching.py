from data_fetcher import DataFetcher

# Not ready to implement anything in crypto but adding for future use cases.
def test_crypto_data():
    data_fetcher = DataFetcher()
    crypto_symbol = 'BTC/USDT'
    crypto_data = data_fetcher.fetch_crypto_data(crypto_symbol)
    if crypto_data is not None:
        data_fetcher.save_data(crypto_data, crypto_symbol, data_type='crypto')


if __name__ == "__main__":
    stock_symbol = input("Crypto:")
    test_crypto_data()