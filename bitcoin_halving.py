import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fetch Bitcoin price data
bitcoin_data = yf.download('BTC-USD', start='2012-01-01', end='2023-01-01')

# Convert the date column to datetime format
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data.index)

# Visualize the distribution of Bitcoin prices
plt.figure(figsize=(12, 6))
plt.plot(bitcoin_data['Date'], bitcoin_data['Close'], label='Bitcoin Price (USD)')
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price (USD)')
plt.legend()
plt.show()