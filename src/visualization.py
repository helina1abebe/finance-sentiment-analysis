import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_with_indicators(df, ticker):
    """
    Plot closing price with SMA and EMA.
    :param df: DataFrame with stock data.
    :param ticker: Stock ticker symbol.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["Close"], label="Close Price", color="blue")
    plt.plot(df.index, df["SMA_10"], label="SMA 10", color="orange")
    plt.plot(df.index, df["EMA_10"], label="EMA 10", color="green")
    plt.title(f"{ticker} Price and Indicators")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()

def plot_rsi(df, ticker):
    """
    Plot RSI.
    :param df: DataFrame with stock data.
    :param ticker: Stock ticker symbol.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["RSI"], label="RSI", color="purple")
    plt.axhline(70, color="red", linestyle="--", label="Overbought (70)")
    plt.axhline(30, color="green", linestyle="--", label="Oversold (30)")
    plt.title(f"{ticker} RSI")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid()
    plt.show()

def plot_macd(df, ticker):
    """
    Plot MACD and Signal Line.
    :param df: DataFrame with stock data.
    :param ticker: Stock ticker symbol.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["MACD"], label="MACD", color="blue")
    plt.plot(df.index, df["MACD_Signal"], label="Signal Line", color="orange")
    plt.title(f"{ticker} MACD")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()
    plt.show()
