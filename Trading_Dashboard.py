import streamlit as st
import Tickers

#
# Call all the init functions
#
Tickers.readAllPriceCsv()
Tickers.readTickerInfo()

##st.markdown("# Trading Dashboard")
##st.sidebar.markdown("# Trading Dashboard")

def run():
    st.set_page_config(
        page_title="Trading Dashboard",
        page_icon="👋",
        layout='wide'
    )

    st.write("# Welcome to Trading Dashboard! ")

    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        ### Trading Dashboard Description

        ### Contributors
        - Kamal
        - John
        - Alyssa
        - Patricia
        
        ### Project repo
        - [Trading Dashboard](https://github.com/patricia-raj/financial-market-trading-dashboard)
        
    """
    )


if __name__ == "__main__":
    run()
