import os
import pandas as pd

def load_all_stock_data(path: str) -> dict:
    """
    Load all CSV files from the directory and return dict of DataFrames keyed by ticker.
    """
    stock_data = {}
    for file in os.listdir(path):
        if file.endswith(".csv"):
            ticker = file.split("_")[0].upper()
            df = pd.read_csv(os.path.join(path, file))
            stock_data[ticker] = prepare_single_stock_df(df)
    return stock_data

def prepare_single_stock_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare a single stock DataFrame.
    """
    required_columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in stock data: {missing_cols}")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    df.set_index("Date", inplace=True)
    df.fillna(method="ffill", inplace=True)
    df.dropna(inplace=True)
    return df

