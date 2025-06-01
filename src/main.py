from data_loader import load_all_stock_data
from indicators import add_ta_indicators
from financial_metrics import calculate_all_metrics
from visualization import plot_price_with_indicators, plot_rsi, plot_macd


def main():
    # Load data
    stock_data = load_all_stock_data("data/raw/yfinance_data")

    for ticker, df in stock_data.items():
        # Add indicators
        df = add_ta_indicators(df)
        
        # Calculate metrics
        metrics = calculate_all_metrics(df)
        print(f"Metrics for {ticker}: {metrics}")

        # Visualize
        plot_price_with_indicators(df, ticker)
        plot_rsi(df, ticker)
        plot_macd(df, ticker)

if __name__ == "__main__":
    main()