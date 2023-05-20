import time
import subprocess
import yfinance as yf
import datetime
import pandas as pd
import schedule
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter

start_time = "18:51"
stop_time = datetime.time(hour=19, minute=30, second=0)

date1 = []
time1 = []
bitcoin1 = []
mbb1 = []
now1 = []
bitcoinlow = []
bitcoinhigh = []
bitcoinopen = []
bitcoinvolume = []
minutes_from_midnight = []
midnight = datetime.time(hour=0, minute=0, second=0)
from datetime import date
today = date.today()


def job():

    while datetime.datetime.now().time() < stop_time:
        
        for i in range(10):
            """
            tickerSymbol = '^DJI'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPrice = tickerData.history(period='1d')['Close'][0]
            
            print('The current price of the Dow Jones index is:', tickerPrice)
            """    
            tickerSymbolmbb = '1155.KL'
            tickerData = yf.Ticker(tickerSymbolmbb)
            tickerPricembb = tickerData.history(period='1d')['Close'][0]
            
            print('The current price of the Maybank share is:', tickerPricembb)
            
            tickerSymbol = 'USDMYR=X'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPrice = tickerData.history(period='1d')['Close'][0]
            
            print('The current USD/MYR exchange rate is:', tickerPrice)
            
            tickerSymbol = 'BTC-USD'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPricebit = tickerData.history(period='1d')['Close'][0]
            
            print('The current BTC-USD price is:', tickerPricebit)
            
            tickerSymbol = 'BTC-USD'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPricebitopen = tickerData.history(period='1d')['Open'][0]
            
            print('The open BTC-USD price is:', tickerPricebitopen)
            
            tickerSymbol = 'BTC-USD'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPricebithigh = tickerData.history(period='1d')['High'][0]
            
            print('The high BTC-USD price is:', tickerPricebithigh)
            
            tickerSymbol = 'BTC-USD'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPricebitlow = tickerData.history(period='1d')['Low'][0]
            
            print('The low BTC-USD price is:', tickerPricebitlow)
            
            tickerSymbol = 'BTC-USD'
            tickerData = yf.Ticker(tickerSymbol)
            tickerPricebitvol = tickerData.history(period='1d')['Volume'][0]
            
            print('The volume of BTC-USD price is:', tickerPricebitvol)
            
        
            now = datetime.datetime.now()
            current_date = now.date()
            current_time = now.time()
            datetime2 = datetime.datetime.combine(current_date, midnight)
            datetime1 = datetime.datetime.combine(current_date, current_time)
            time_elapsed = datetime1 - datetime2
            total_minutes = round(time_elapsed.total_seconds()/60)
         
            
            print('The current time is:', current_time)
            print('The current date is:', current_date)
            
            date1.append(current_date)
            time1.append(current_time)
            bitcoin1.append(tickerPricebit)
            mbb1.append(tickerPricembb)
            now1.append(now)
            bitcoinopen.append(tickerPricebitopen)
            bitcoinhigh.append(tickerPricebithigh)
            bitcoinlow.append(tickerPricebitlow)
            bitcoinvolume.append(tickerPricebitvol)
            minutes_from_midnight.append(total_minutes)


            print("date length", len(date1))
            print("time length", len(time1))
            print("bitcoin length", len(bitcoin1))
            print("mbb length", len(mbb1))
            
            print(" ")
            time.sleep(60)
        print("meow")

        
        # Create a figure and axes
        fig, ax = plt.subplots()

        # Plot the data
        ax.scatter(now1,bitcoin1)
        #graph formatting     
        ax.tick_params(which='major', width=2.00)
        ax.tick_params(which='minor', width=2.00)
        ax.xaxis.label.set_fontsize(15)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(15)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        plt.xlabel("Time")
        plt.ylabel("Bitcoin Price (USD)")
        # Set x-axis formatter
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        # Set the locator for 5 tickers
        ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5))
        
        # Rotate tick labels
        plt.xticks(rotation=45)
        
        # Display the plot
        plt.show()
        plt.close()
        
        
        # Create a figure and axes
        fig, ax = plt.subplots()

        # Plot the data
        ax.scatter(minutes_from_midnight,bitcoin1)
        #graph formatting     
        ax.tick_params(which='major', width=2.00)
        ax.tick_params(which='minor', width=2.00)
        ax.xaxis.label.set_fontsize(15)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(15)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        plt.xlabel("Time")
        plt.ylabel("Bitcoin Price (USD)")

        
        # Display the plot
        plt.show()
        plt.close()

        


j = schedule.every().day.at(start_time).do(job)

while datetime.datetime.now().time() < stop_time:
    schedule.run_pending()


    

"""
import datetime

now = datetime.datetime.now()

# Separate date and time components
current_date = now.date()
current_time = now.time()

print("Current date: ", current_date)
print("Current time: ", current_time)


import yfinance as yf
tickerSymbol = '1155.KL'
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for the last 5 years
tickerDf = tickerData.history(period='5y')

print(tickerDf)

import yfinance as yf

tickerSymbol = '1155.KL'
tickerData = yf.Ticker(tickerSymbol)

# get the historical trading volume for the last 5 years
tickerDf = tickerData.history(period='5y', actions=False)['Volume']

print(tickerDf)

"""