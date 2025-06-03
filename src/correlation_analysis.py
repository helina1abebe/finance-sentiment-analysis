import pandas as pd

def align_dates(stock_df: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Align stock data and news sentiment data by date.
    Assumes stock_df indexed by Date, news_df has 'Date' and 'sentiment' columns.
    """
    news_df['Date'] = pd.to_datetime(news_df['Date'])
    # Aggregate sentiment by date (mean)
    daily_sentiment = news_df.groupby('Date')['sentiment'].mean().reset_index()

    stock_reset = stock_df.reset_index()

    merged_df = pd.merge(stock_reset, daily_sentiment, on='Date', how='left')
    merged_df['sentiment'].fillna(0, inplace=True)  # or keep NaN if preferred
    merged_df.set_index('Date', inplace=True)

    return merged_df

def calculate_daily_returns(df: pd.DataFrame) -> pd.Series:
    """
    Calculate daily returns from 'Close' prices.
    """
    returns = df['Close'].pct_change()
    return returns

def calculate_correlation(df: pd.DataFrame) -> float:
    """
    Calculate Pearson correlation between daily returns and sentiment.
    """
    returns = calculate_daily_returns(df)
    sentiment = df['sentiment']

    # Align lengths, drop NaNs
    combined = pd.concat([returns, sentiment], axis=1).dropna()
    if combined.empty:
        return float('nan')
    corr = combined.iloc[:,0].corr(combined.iloc[:,1])
    return corr
