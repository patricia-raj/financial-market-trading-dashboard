import streamlit as st
import yfinance as yf
import pandas as pd
import Tickers 



st.set_page_config(layout='wide')
##Sets to wider page configuration and Title to obtain good visualization """
st.title('Real-Time - Cumulative Return and Volume Comparison' )

##Fetches Stock list 
tickers = Tickers.nasdaq_100

 
##Configure user interactions such as assest selection and period for stock analysis

dropdown = st.multiselect( 'Pick vour assets', tickers)
start = st.date_input('Start',value = pd.to_datetime('2021-01-01'))
end = st.date_input ('End', value = pd.to_datetime('today'))

def relative_returns(close_price_df):
    ###Stock prices are in different currencies and to get a general view of the performance and to view that in the same unit or metric. Relative returns is calculated using ticker close price
        ## Parameter: close_price_df - Dataframe containing close price of the selected ticker(s)
        ## Returns: cumret - Cumulative returns is calculated for the close price.
    ###
    
    rel = close_price_df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len (dropdown) > 0:
    
    ## Fetches Stock Close price from Yahoo Finance 
    close_df = yf.download(dropdown,start,end)['Close']
    return_df = relative_returns(close_df)
    
    ## Plots the stock returns  
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(return_df,width=1000, height=500, use_container_width=True)
    
    ## Fetches Volume from Yahoo Finance  
    volume_df = yf.download(dropdown,start,end)['Volume']
    
    ## Plots the Volume to compare it with Returns  
    st.header('Volume of {}'.format(dropdown))
    st.bar_chart(volume_df,width=1000, height=500, use_container_width=True)