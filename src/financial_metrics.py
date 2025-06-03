#Why PyNance is Not Used
#Custom Implementation: Calculations are manually implemented, avoiding external libraries.
#Flexibility: pandas and numpy offer more control.
#No Extra Dependencies: Reduces the need for managing additional libraries.

import pandas as pd
import numpy as np

def calculate_returns(df):
    """
    Calculate daily returns and cumulative returns.
    :param df: DataFrame with stock data.
    :return: Tuple (daily returns, cumulative returns).
    """
    daily_returns = df["Close"].pct_change()
    cumulative_returns = (1 + daily_returns).cumprod()
    return daily_returns, cumulative_returns

def calculate_volatility(daily_returns):
    """
    Calculate annualized volatility.
    :param daily_returns: Series of daily returns.
    :return: Annualized volatility.
    """
    return daily_returns.std() * np.sqrt(252)  # 252 trading days in a year

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01):
    """
    Calculate Sharpe ratio.
    :param daily_returns: Series of daily returns.
    :param risk_free_rate: Risk-free rate (default: 1%).
    :return: Sharpe ratio.
    """
    excess_returns = daily_returns - risk_free_rate / 252
    return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

def calculate_all_metrics(df):
    """
    Calculate financial metrics for the stock.
    :param df: DataFrame with stock data.
    :return: Dictionary of metrics.
    """
    daily_returns, cumulative_returns = calculate_returns(df)
    metrics = {
        "Annualized Volatility": calculate_volatility(daily_returns),
        "Sharpe Ratio": calculate_sharpe_ratio(daily_returns),
        "Cumulative Return": cumulative_returns.iloc[-1],
    }
    return metrics

