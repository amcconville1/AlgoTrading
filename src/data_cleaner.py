import pandas as pd
import os

class DataCleaner:
    def __init__(self, df):
        """Initialize the DataCleaner with a DataFrame."""
        self.df = df

    def handle_missing_values(self, strategy='drop'):
        """Handle missing values in the DataFrame.
        
        Args:
            strategy (str): Strategy to handle missing values ('drop' or 'fill').
                - 'drop': Drop rows with missing values.
                - 'fill': Forward fill missing values using the previous valid value.

        Raises:
            ValueError: If the strategy is not 'drop' or 'fill'.
        """
        if strategy == 'drop':
            self.df.dropna(inplace=True)
        elif strategy == 'fill':
            self.df.fillna(method='ffill', inplace=True)
        else:
            raise ValueError("Strategy not recognized. Use 'drop' or 'fill'.")

    def set_timestamp_index(self):
        """Convert the DataFrame's index to datetime if it's not already."""
        self.df.index = pd.to_datetime(self.df.index)

    def clean(self, missing_value_strategy='drop'):
        """Run all cleaning steps on the DataFrame.
        
        Args:
            missing_value_strategy (str): Whether to 'drop' or 'fill' missing values.
        
        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        self.handle_missing_values(strategy=missing_value_strategy)
        self.set_timestamp_index()
        return self.df


def clean_all_stock_files(data_dir='data/stocks', cleaned_data_dir='data/cleaned_stocks'):
    """Clean all stock data files in the given directory and save them to a cleaned directory.

    Args:
        data_dir (str): Path to the directory containing raw stock CSV files.
        cleaned_data_dir (str): Path to the directory where cleaned CSV files will be saved.
    """
    # Ensure the directory for cleaned data exists
    os.makedirs(cleaned_data_dir, exist_ok=True)

    # Iterate over all CSV files in the stock data directory
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(data_dir, filename)

            # Load the CSV file into a DataFrame
            print(f"Cleaning file: {filename}")
            df = pd.read_csv(file_path)

            # Initialize the DataCleaner class with the loaded DataFrame
            cleaner = DataCleaner(df)

            # Clean the data (drop missing values and set timestamp as index)
            df_cleaned = cleaner.clean(missing_value_strategy='drop')  # or 'fill'

            # Save the cleaned data to the new directory
            cleaned_file_path = os.path.join(cleaned_data_dir, filename)
            df_cleaned.to_csv(cleaned_file_path, index=False)
            print(f"Cleaned file saved: {cleaned_file_path}")
