import streamlit as st
import yfinance as yf
import pandas as pd
import Tickers 

st.set_page_config(layout='wide')
st.title('Real-Time - Stock Financial Information' )
tickers = Tickers.nasdaq_100

## User Interaction
dropdown = st.selectbox('Pick vour assets', tickers)


if len (dropdown) > 0:
    stock = yf.Ticker(dropdown)
    
    # Display an interactive table
    stockearn = stock.earnings
    earn_df = pd.DataFrame(stockearn)
    with st.container():
        st.header('Earnings of {}'.format(dropdown))
        ## Split into two columns to visualize earnings and Revenues along view the raw information
        earn_chart, earn_data = st.columns(2)

        with earn_chart:
            st.bar_chart(earn_df,width=1000, height=500, use_container_width=True)
        with earn_data:
            st.write(stockearn)
    
    ## Getting Daily High and Low along with Fity two weeks high and low.
    st.header('Stock Price High and Low - {}'.format(dropdown))
    price = [stock.info['dayHigh'], stock.info['dayLow'], stock.info['fiftyTwoWeekHigh'], stock.info['fiftyTwoWeekLow']]
    index = ["Day High", "Day Low", "Year High", "Year Low"]
    phl = pd.DataFrame({"HighLow": index, "Price": price})
    phl.set_index('HighLow')
    phl = phl.astype(str)
    st.dataframe(phl)
    
    ## Obtain Financial information for a stock.
    st.header('Financials - {}'.format(dropdown))
    stockfin = stock.financials
    fin_df = pd.DataFrame(stockfin)
    fin_df.dropna(inplace=True)
    fin_df = fin_df.transpose()
    fin_df.index = pd.to_datetime(fin_df.index, format = '%Y-%m-%d')
    fin_df.index = fin_df.index.strftime('%Y')
    st.dataframe(fin_df)
    
    ## Fetch Recommendation information for a stock.
    st.header('Recommendations - {}'.format(dropdown))
    stockreco = stock.recommendations
    st.dataframe(stockreco)
    
    ## Get insight on Major share holders.
    st.header('Major Holders - {}'.format(dropdown))
    stockholders = stock.major_holders
    holders_df = pd.DataFrame(stockholders)
    holders_df.rename({0: 'Percent', 1: 'Share Holders'},axis=1, inplace=True)
    holders_df = holders_df[['Share Holders','Percent']]
    st.dataframe(holders_df)
    
    
    ## Analysis Dvident information.
    st.header('Divident Information - {}'.format(dropdown))
    stockdiv = stock.dividends
    st.dataframe(stockdiv)
    