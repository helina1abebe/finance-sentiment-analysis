import os
import pandas as pd

def load_all_stock_data(path: str) -> dict:
    """
    Load all CSV files from the specified directory and return a dictionary of DataFrames.
    :param path: Path to the folder containing CSV files.
    :return: Dictionary where keys are stock tickers and values are DataFrames.
    """
    stock_data = {}
    for file in os.listdir(path):
        if file.endswith(".csv"):
            ticker = file.split("_")[0].upper()  # Extract ticker from file name
            df = pd.read_csv(os.path.join(path, file))
            stock_data[ticker] = prepare_single_stock_df(df)
    return stock_data

def prepare_single_stock_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare a single stock's DataFrame.
    :param df: Raw stock data DataFrame.
    :return: Cleaned and prepared DataFrame.
    """
    # Ensure essential columns are present
    required_columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in data: {missing_cols}")
    
    # Parse dates and set index
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    
    # Handle missing values
    df = df.sort_index()
    df.fillna(method="ffill", inplace=True)  # Forward fill missing values
    df.dropna(inplace=True)  # Drop rows with remaining nulls
    
    return df
