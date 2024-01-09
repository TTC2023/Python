import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

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

# Halving dates
halving_dates = ['2012-11-28', '2016-07-09', '2020-05-11']

# Assuming 'halving_dates' contains the halving dates
pre_halving_data = bitcoin_data[bitcoin_data['Date'].isin(halving_dates) == False]
post_halving_data = bitcoin_data[bitcoin_data['Date'].isin(halving_dates) == True]


# Perform t-test
t_stat, p_value = ttest_ind(pre_halving_data['Close'], post_halving_data['Close'])

# Display the results
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

plt.figure(figsize=(12, 6))
plt.plot(pre_halving_data['Date'], pre_halving_data['Close'], label='Before Halving')
plt.plot(post_halving_data['Date'], post_halving_data['Close'], label='After Halving')
plt.title('Bitcoin Price Trends Before and After Halving Events')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price (USD)')
plt.legend()
plt.show()
