# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:41:04 2023

@author: limyu
"""
import time
import subprocess
import yfinance as yf
import datetime
import pandas as pd
import schedule
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

start_time = "11:46"
stop_time = datetime.time(hour=12, minute=10, second=0)

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

# Define the target time in seconds from the current time
target_time = time.time() + 1200  # 6000 seconds from now

# Loop until the current time exceeds the target time
while time.time() < target_time:
    
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
        print('Stop time', stop_time)
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
    
    dfbit = pd.DataFrame()
    dfbit["price"] = bitcoin1
    dfbit["minute"] = minutes_from_midnight
    dfbit["volume"] = bitcoinvolume
    
    from sklearn.preprocessing import MinMaxScaler

    def normalize_list(lst):
        scaler = MinMaxScaler(feature_range=(0, 1))
        normalized_list = scaler.fit_transform([[value] for value in lst])
        return [value[0] for value in normalized_list]
    bitcoin1_norm = normalize_list(bitcoin1)
    minutes_from_midnight_norm = [i/1440 for i in minutes_from_midnight]
    bitcoinlow_norm = normalize_list(bitcoinlow)
    bitcoinhigh_norm = normalize_list(bitcoinhigh)
    bitcoinopen_norm = normalize_list(bitcoinopen)
    bitcoinvolume_norm = normalize_list(bitcoinvolume)
    
    dfbit_norm = pd.DataFrame()
    dfbit_norm["price"] = bitcoin1_norm
    dfbit_norm["minute"] = minutes_from_midnight_norm
    dfbit_norm["volume"] = bitcoinvolume_norm
    
    print(dfbit_norm.columns)
    
    col_feature = ['minute', 'volume']
    dfbit_fea = dfbit_norm[col_feature]
    col_label = ['price']
    dfbit_label = dfbit_norm[col_label]
    
    X = dfbit_fea
    y = dfbit_label
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = Sequential()
    model.add(Dense(len(X_train.keys()),  input_shape=[len(X_train.keys())]))
    name = []
    mae = []
    nodes = []
    layers1=[]
    ape_actual = []
    dense_layers = [2,5,8]
    layer_sizes = [5,10,20]
    


    for dense_layer in dense_layers:
        for layer_size in layer_sizes:
            NAME = "{}-nodes-{}-dense-{}".format(layer_size, dense_layer, int(time.time()))
            print(NAME)
            name.append(NAME)
            nodes.append(layer_size)
            layers1.append(dense_layer)
    
            for _ in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('elu'))
            model.add(Dense(y_train.shape[1]))
            
            # Compile the model
            model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
            
            # Train the model
            history = model.fit(X_train, y_train, epochs=50, validation_split=0.3)
            
            # Evaluate the model
            loss1, mae1 = model.evaluate(X_test, y_test)
            
            # Print the results
            print('Mean Absolute Error:', mae1)
            print('loss', loss1)
            mae.append(mae1)
    df_mae = pd.DataFrame()
    df_mae["name"] = name
    df_mae["mae"] = mae
    df_mae["number of layers"] = layers1
    df_mae["number of nodes first layer"] = nodes
    min_index = mae.index(min(mae))
    

    model1 = Sequential()
    model1.add(Dense(len(X_train.keys()),  input_shape=[len(X_train.keys())]))
    for _ in range(layers1[min_index]):
        model1.add(Dense(nodes[min_index]))
        model1.add(Activation('elu'))
    model1.add(Dense(y_train.shape[1]))
    
    # Compile the model
    model1.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
    # Train the model
    history1 = model1.fit(X_train, y_train, epochs=50, validation_split=0.3)
    
    bitcoin1_benchmark = []
    
    minutes_from_midnight_pred = []
    bitcoinlow_pred = []
    bitcoinhigh_pred = []
    bitcoinopen_pred = []
    bitcoinvolume_pred = []
    
    for i in range(10):
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
     
        bitcoin1.append(tickerPricebit)
        minutes_from_midnight.append(total_minutes)
        bitcoinlow.append(tickerPricebitlow)
        bitcoinhigh.append(tickerPricebithigh)
        bitcoinopen.append(tickerPricebitopen)
        bitcoinvolume.append(tickerPricebitvol)
        

        bitcoin1_benchmark.append(tickerPricebit)
        minutes_from_midnight_pred.append(total_minutes)
        bitcoinlow_pred.append(tickerPricebitlow)
        bitcoinhigh_pred.append(tickerPricebithigh)
        bitcoinopen_pred.append(tickerPricebitopen)
        bitcoinvolume_pred.append(tickerPricebitvol)
        

        print(" ")
        time.sleep(60)
    minutes_from_midnight_pred_norm = [i/1440 for i in minutes_from_midnight_pred]
    bitcoinlow_pred_norm = [(i - min(bitcoinlow))/(max(bitcoinlow)-min(bitcoinlow)) for i in bitcoinlow_pred]
    bitcoinhigh_pred_norm = [(i - min(bitcoinhigh))/(max(bitcoinhigh)-min(bitcoinhigh)) for i in bitcoinhigh_pred]
    bitcoinopen_pred_norm = [(i - min(bitcoinopen))/(max(bitcoinopen)-min(bitcoinopen)) for i in bitcoinopen_pred]
    bitcoinvolume_pred_norm = [(i - min(bitcoinvolume))/(max(bitcoinvolume)-min(bitcoinvolume)) for i in bitcoinvolume_pred]
    X_pred = pd.DataFrame()
    X_pred['minute'] = minutes_from_midnight_pred_norm
    X_pred['volume'] = bitcoinvolume_norm[0]
    predictions = model1.predict(X_pred)
    bitcoin_pred = [(i*(max(bitcoin1)-min(bitcoin1)))+min(bitcoin1) for i in predictions]
    
    fig = plt.figure(figsize=(7, 4))
    ax = plt.axes()
    ax.scatter(minutes_from_midnight_pred, bitcoin_pred, color = "blue")
    ax.scatter(minutes_from_midnight_pred, bitcoin1_benchmark, color = "red")
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
    plt.xlabel("Height from grating (µm)")
    plt.ylabel("Vertical Beam Waist")
    plt.legend(["Predicted Price", "Actual Price"], prop={'weight': 'bold','size': 10}, loc = "upper left")
    plt.show()
    plt.close()
    

