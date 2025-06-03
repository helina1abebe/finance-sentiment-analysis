from textblob import TextBlob
import pandas as pd

def compute_sentiment(news_df: pd.DataFrame, text_column: str = 'headline') -> pd.DataFrame:
    """
    Add a 'sentiment' column to news_df based on polarity of text_column.
    :param news_df: DataFrame with news data.
    :param text_column: Column containing the text for sentiment analysis.
    :return: DataFrame with added 'sentiment' column.
    """
    if text_column not in news_df.columns:
        raise ValueError(f"Column '{text_column}' not found in news data.")

    # Compute polarity score for each text entry
    news_df['sentiment'] = news_df[text_column].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    return news_df
