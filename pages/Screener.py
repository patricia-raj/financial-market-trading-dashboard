import streamlit as st
import Tickers
import pandas as pd


def generateDf(columnList, rowList):
    df = pd.DataFrame(rowList, columns=columnList)
    df = df.set_index('Ticker')
    return df

#
# Streamlit code:
#
st.markdown("# Stock screener ❄️")
st.sidebar.markdown("# Screener categories ❄️")
st.markdown("### Testing stocks in the nasdaq 100...")


#
# Walk through the nasdaq 100 & create an entry for each:
#
columnList = ['Ticker', 'Close', 'Week', 'Month', 'YTD', 'Year']
rowList = []
for ticker in Tickers.nasdaq_100:
    l = [ticker, Tickers.tickerPriceInfo[ticker].iloc[0]['Close'],
         0, 0, 0, 0]
    rowList.append(l)

df = generateDf(columnList, rowList)

st.table(df)
