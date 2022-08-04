import streamlit as st
import yfinance as yf
import pandas as pd
import Tickers 

st.set_page_config(layout='wide')
st.title('Real-Time - Stock Information' )
tickers = Tickers.nasdaq_100


dropdown = st.selectbox('Pick vour assets', tickers)
if len (dropdown) > 0:
    stock = yf.Ticker(dropdown)
    
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    # Display an interactive table
    
    #st.header('Stock Information of {}'.format(dropdown))
    #st.write(stock.info.keys())
    #stockinfo_df = pd.DataFrame(stock.info)
    #st.table(stockinfo_df)
    #stock_info = stockinfo_df[['totalCash', 'totalDebt','totalRevenue']
    #st.dataframe(stock_info)
    #stockcalendar = stock.calendar
    #st.write(stockcalendar)
    st.header('Financials of {}'.format(dropdown))
    stockfin = stock.financials
    st.write(stockfin)
    st.header('Earnings of {}'.format(dropdown))
    stockearn = stock.earnings
    st.write(stockearn)
    st.header('Divident Information of {}'.format(dropdown))
    stockdiv = stock.dividends
    st.write(stockdiv)
    st.header('Recommendations of {}'.format(dropdown))
    stockreco = stock.recommendations
    st.write(stockreco)
    st.header('Major Holders of {}'.format(dropdown))
    stockholders = stock.major_holders
    st.write(stockholders)
    