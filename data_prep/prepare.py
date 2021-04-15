import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
#-------------------------------------------------------------------------------------------------------------------------------------

def pull_OPS_csv(url):

    req = requests.get(url)
    data = StringIO(req.text)
    df = pd.read_csv(data)
    df = pd.DataFrame(df)
    return df
    df = df.to_csv('Open_Power_Systems_Data')
    
#-------------------------------------------------------------------------------------------------------------------------------------

def prep_OPS_data(df):
    # Reassign the sale_date column to be a datetime type
    df.Date = pd.to_datetime(df.Date)

    # Plot distributions for each feature
    plt.figure(figsize=(20, 30))
    
    plt.subplot(10,1,1)
    df.Consumption.plot()
    
    plt.subplot(10,1,2)
    df.Solar.plot()
    
    plt.subplot(10,1,3)
    df['Wind+Solar'].plot()

    # Sort rows by the date and then set the index as that date
    df = df.set_index("Date", drop=False).sort_index()

    # Create new columns for month and year
    df['month'] = pd.DatetimeIndex(df.Date).month
    df['year'] = pd.DatetimeIndex(df.Date).year

    # Sort rows by the date and then set the index as that date
    df = df.set_index("Date").sort_index()
    
    # Fills any missing/na values using bfill method
    df = df.fillna(method='bfill')
    return df

#-------------------------------------------------------------------------------------------------------------------------------------