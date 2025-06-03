### 📊 Financial News and Stock Price Analysis

This project analyzes financial news and stock price data to uncover insights about analyst ratings, publisher activities, and emerging trends over time.

---

### 🗂️ Project Structure

```
📁 .github/  
    └── workflows/  
        └── unittests.yml       # 🚀 CI/CD pipeline for tests  
📁 .vscode/  
    └── settings.json           # ⚙️ VS Code configurations  
📁 data/  
    ├── raw/  
    │   ├── yfinance_data/      # 📈 Historical stock data  
    │   │   ├── AAPL_historical_data.csv  
    │   │   ├── AMZN_historical_data.csv  
    │   │   ├── GOOG_historical_data.csv  
    │   │   ├── META_historical_data.csv  
    │   │   ├── MSFT_historical_data.csv  
    │   │   ├── NVDA_historical_data.csv  
    │   │   └── TSLA_historical_data.csv  
    │   └── raw_analyst_ratings.csv # 📰 News/ratings data  
    └── processed/              # ✅ Cleaned or transformed data (optional)  
📁 notebooks/  
    ├── Headline_EDA.ipynb      # 🧪 Exploratory analysis of headlines  
    ├── stock_analysis.ipynb    # 📊 Stock data analysis notebook  
    ├── optimal_lda_model.gensim  # 📚 Optimal LDA model  
    ├── optimal_lda_model.gensim.*  # 🛠️ Associated LDA files  
    └── README.md               # 📖 Notebook descriptions  
📁 scripts/  
    └── README.md               # 🗒️ Utility script descriptions  
📁 src/  
    ├── __init__.py             # 🛠️ Initialize package  
    ├── data_loader.py          # 📂 Data loading and cleaning functions  
    ├── financial_metrics.py    # 📊 Technical indicators (MA, RSI, MACD)  
    ├── main.py                 # 🎯 Main analysis pipeline  
    ├── visualization.py        # 📈 Plotting and visualizations  
    └── nlp_processing.py       # 🧠 Text processing and sentiment analysis  
📁 tests/  
    ├── __init__.py             # 🛠️ Initialize test package  
📄 .gitignore                   # 🚫 Files to ignore in Git  
📄 README.md                    # 📖 Main project documentation  
📄 requirements.txt             # 🧩 Python dependencies  
```

---

### 🏁 Getting Started

#### 🔧 Install Dependencies

Run the following command to install required packages:

```bash
pip install -r requirements.txt  
```

#### 📂 Run the Notebook

Open `notebooks/Headline_EDA.ipynb` and `notebooks/stock_analysis.ipynb` in Jupyter Notebook or VS Code to explore the data and visualizations.

---

### 📚 Data Sources

* **Data/raw\_analyst\_ratings.csv**: Dataset of analyst ratings.
* **Data/yfinance\_data/**: Historical stock price data for selected tickers.

---

### 📊 Visualizations

The notebook provides insights such as:

* 📰 Top headlines and their frequencies.
* 🏢 Article counts per publisher.
* 🗓️ Distribution of articles by day of the week and month.

---

### 🔄 Continuous Integration

✅ Unit tests are automatically run via GitHub Actions.

---

### 📜 License

Licensed under MIT. Consider adding a `LICENSE` file for clarity.
