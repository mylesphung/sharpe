# import packages
import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# format graph
plt.style.use('fivethirtyeight')

# override yahoo finance thing
yf.pdr_override()

# get stocks and benchmark
stockOne = str(input("First Stock (Ticker): ")).upper()
stockTwo = str(input("Second Stock (Ticker): ")).upper()
bench = str(input("Benchmark (Ticker): ")).upper()

# reading the data
stockData = pdr.get_data_yahoo((stockOne+" "+stockTwo), period="1y").dropna()
benchData = pdr.get_data_yahoo(bench, period="1y").dropna()

# print stock data
print("Stocks:\n")
stockData.info()
print(stockData.head())

# print benchmark data
print("Benchmark:\n")
benchData.info()
benchData.head()

# visualize and describe the stock data
stockData['Close'].plot(
    title="Stock Data");
stockData.describe()

# visualize the benchmark data
benchData['Close'].plot(label=bench.upper(), legend='upperleft');
benchData.describe()

# show plots
plt.show()

# calculate, describe, and plot daily stock returns
stockReturns = stockData['Close'].pct_change()
stockReturns.plot(title="Daily Stock Returns")

# calculate, describe, and plot daily benchmark returns
benchReturns = benchData['Close'].pct_change()
benchReturns.plot(label=bench.upper(), legend='upperleft')

# show plots
plt.show()

# calculate and plot difference in daily returns
excessReturns = stockReturns.sub(benchReturns, axis=0)
excessReturns.plot(title="Excess Returns")
plt.show()

# calculate and plot the mean of excess returns
avg_excess_return = excessReturns.mean()
avg_excess_return.plot.bar(title="Mean of the Return Difference", rot=0)
plt.show()

# calculate and plot the standard deviations
sd_excessReturn = excessReturns.std()
sd_excessReturn.plot.bar(title="Standard Deviation of the Return Difference", rot=0)
plt.show()

# calculate the daily sharpe ratio
dailySharpe = avg_excess_return.div(sd_excessReturn)

# annualize ratio and plot
annualFactor = np.sqrt(252)
annualSharpe = dailySharpe.mul(annualFactor)
annualSharpe.plot.bar(title="Annualized Sharpe Ratios", rot=0)
plt.show()