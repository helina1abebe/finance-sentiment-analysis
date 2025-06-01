import talib

def add_ta_indicators(df):
    """
    Add technical indicators to the DataFrame.
    :param df: DataFrame with stock data.
    :return: DataFrame with added indicators.
    """
    # Simple Moving Averages (SMA)
    df["SMA_10"] = talib.SMA(df["Close"], timeperiod=10)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
    
    # Exponential Moving Averages (EMA)
    df["EMA_10"] = talib.EMA(df["Close"], timeperiod=10)
    
    # Relative Strength Index (RSI)
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
    
    # MACD
    df["MACD"], df["MACD_Signal"], df["MACD_Hist"] = talib.MACD(
        df["Close"], fastperiod=12, slowperiod=26, signalperiod=9
    )
    
    return df
