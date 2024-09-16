import pandas as pd
import matplotlib.pyplot as plt

class StockAnalyzer:
    def __init__(self, stock_file):
        """Initialize the StockAnalyzer with the stock file (CSV)."""
        self.stock_file = stock_file
        self.df = None  # Placeholder for the DataFrame

    def load_data(self):
        """Load the stock data from the CSV file (no explicit date handling)."""
        # Load the CSV without trying to convert the index to dates
        self.df = pd.read_csv(self.stock_file)
        return self.df

    def calculate_moving_average(self, window=50):
        """Calculate the moving average for the given window size."""
        column_name = f'SMA_{window}'
        self.df[column_name] = self.df['Close'].rolling(window=window).mean()
        return self.df

    def calculate_volatility(self, window=20):
        """Calculate the rolling volatility (standard deviation) for the given window size."""
        column_name = f'Volatility_{window}'
        self.df[column_name] = self.df['Close'].rolling(window=window).std()
        return self.df

    def calculate_rsi(self, window=14):
        """Calculate the Relative Strength Index (RSI)."""
        delta = self.df['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        
        rs = avg_gain / avg_loss
        self.df['RSI'] = 100 - (100 / (1 + rs))
        return self.df

    def plot(self, columns=['Close']):
        """Plot the selected columns of the DataFrame."""
        self.df[columns].plot(figsize=(10, 6))
        plt.title(f'{self.stock_file} Stock Analysis')
        plt.show()

    def save_to_csv(self, output_file):
        """Save the analyzed DataFrame to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        print(f'Saved analysis to {output_file}')
