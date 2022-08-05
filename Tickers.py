import pandas as pd

index_etf = []
sector_etf = ["Basic Materials",
              "Telecomms Sector",
              "Utilities Sector",
              "Consumer Discretion",
              "Consumer Staples",
              "Health",
              "Industrial",
              "Technology"]
nasdaq_100 = ["AAPL",
              "MSFT",
              "GOOG",
              "GOOGL",
              "AMZN",
              "TSLA",
              "META",
              "NVDA",
              "PEP",
              "COST",
              "ASML",
              "AVGO",
              "AZN",
              "CMCSA",
              "CSCO",
              "ADBE",
              "QCOM",
              "TMUS",
              "INTC",
              "TXN",
              "AMD",
              "AMGN",
              "HON",
              "INTU",
              "JD",
              "CHTR",
              "NFLX",
              "PYPL",
              "SBUX",
              "ADP",
              "AMAT",
              "MDLZ",
              "ADI",
              "ISRG",
              "GILD",
              "BKNG",
              "VRTX",
              "PDD",
              "CSX",
              "MU",
              "MRNA",
              "REGN",
              "NTES",
              "LRCX",
              "FISV",
              "ABNB",
              "ATVI",
              "KDP",
              "SNPS",
              "MNST",
              "PANW",
              "MAR",
              "KLAC",
              "TEAM",
              "AEP",
              "BIDU",
              "FTNT",
              "KHC",
              "CDNS",
              "NXPI",
              "ORLY",
              "PAYX",
              "EXC",
              "MRVL",
              "ADSK",
              "CRWD",
              "CTAS",
              "LULU",
              "MELI",
              "XEL",
              "DLTR",
              "WDAY",
              "EA",
              "MCHP",
              "CTSH",
              "WBA",
              "DXCM",
              "SGEN",
              "ZM",
              "IDXX",
              "ILMN",
              "LCID",
              "ODFL",
              "BIIB",
              "PCAR",
              "ROST",
              "VRSK",
              "CPRT",
              "DDOG",
              "FAST",
              "EBAY",
              "SIRI",
              "ANSS",
              "ZS",
              "MTCH",
              "VRSN",
              "ALGN",
              #"CEG",
              "SWKS",
              "SPLK",
              "OKTA",
              "DOCU"]

market_caps = ["All", "Mega", "Large", "Mid"]

sectors = ["All",
           "Materials",
           "Consumer Dis",
           "Consumer Stap",
           "Health Care",
           "Industrials",
           "Tech",
           "Telecom",
           "Utilities"]

tickerPriceInfo = {}

tickerInfo = {}

def readAllPriceCsv():
    for ticker in nasdaq_100:
        df = pd.read_csv('Resources/NASDQ-100-Tickers/' + ticker + '.csv')
        tickerPriceInfo[ticker] = df

def readTickerInfo():
    df = pd.read_csv('Resources/NASDQ-100-Info.csv')
    df = df.set_index('Ticker')
    df['Sector'] = df['Sector'].astype('string') 
    for ticker in nasdaq_100:
        tickerInfo[ticker] = df.loc[ticker].tolist()

XEL_data = pd.read_csv('Resources/NASDQ-100-Tickers/XEL.csv')
CEG_data = pd.read_csv('Resources/NASDQ-100-Tickers/CEG.csv')
EXC_data = pd.read_csv('Resources/NASDQ-100-Tickers/EXC.csv')
XEL_data['Date'] = pd.to_datetime(XEL_data["Date"], dayfirst = True)
XEL_data.set_index(XEL_data['Date'], inplace=True)
XEL_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
XEL_data.rename(columns={'Close': 'XEL Close'}, inplace=True)
EXC_data['Date'] = pd.to_datetime(EXC_data["Date"], dayfirst = True)
EXC_data.set_index(EXC_data['Date'], inplace=True)
EXC_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
EXC_data.rename(columns={'Close': 'EXC Close'}, inplace=True)
CEG_data['Date'] = pd.to_datetime(CEG_data["Date"], dayfirst = True)
CEG_data.set_index(CEG_data['Date'], inplace=True)
CEG_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
CEG_data.rename(columns={'Close': 'CEG Close'}, inplace=True)
         
UTSEC = pd.concat([XEL_data, EXC_data, CEG_data], axis='columns', join='inner')


FAST_data = pd.read_csv('Resources/NASDQ-100-Tickers/FAST.csv')
CPRT_data = pd.read_csv('Resources/NASDQ-100-Tickers/CPRT.csv')
CMCSA_data = pd.read_csv('Resources/NASDQ-100-Tickers/CMCSA.csv')
CSCO_data = pd.read_csv('Resources/NASDQ-100-Tickers/CSCO.csv')
TMUS_data = pd.read_csv('Resources/NASDQ-100-Tickers/TMUS.csv')
AEP_data = pd.read_csv('Resources/NASDQ-100-Tickers/AEP.csv')
AAPL_data = pd.read_csv('Resources/NASDQ-100-Tickers/AAPL.csv')
NVDA_data = pd.read_csv('Resources/NASDQ-100-Tickers/NVDA.csv')
GOOG_data = pd.read_csv('Resources/NASDQ-100-Tickers/GOOG.csv')
ODFL_data = pd.read_csv('Resources/NASDQ-100-Tickers/ODFL.csv')
CSX_data = pd.read_csv('Resources/NASDQ-100-Tickers/CSX.csv')
HON_data = pd.read_csv('Resources/NASDQ-100-Tickers/HON.csv')
MRNA_data = pd.read_csv('Resources/NASDQ-100-Tickers/MRNA.csv')
AZN_data = pd.read_csv('Resources/NASDQ-100-Tickers/AZN.csv')
DXCM_data = pd.read_csv('Resources/NASDQ-100-Tickers/DXCM.csv')
WBA_data = pd.read_csv('Resources/NASDQ-100-Tickers/WBA.csv')
KDP_data = pd.read_csv('Resources/NASDQ-100-Tickers/KDP.csv')
KHC_data = pd.read_csv('Resources/NASDQ-100-Tickers/KHC.csv')
DLTR_data = pd.read_csv('Resources/NASDQ-100-Tickers/DLTR.csv')
MELI_data = pd.read_csv('Resources/NASDQ-100-Tickers/MELI.csv')
TSLA_data = pd.read_csv('Resources/NASDQ-100-Tickers/TSLA.csv')

FAST_data['Date'] = pd.to_datetime(FAST_data["Date"], dayfirst = True)
FAST_data.set_index(FAST_data['Date'], inplace=True)
FAST_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
FAST_data.rename(columns={'Close': 'FAST Close'}, inplace=True)
CPRT_data['Date'] = pd.to_datetime(CPRT_data["Date"], dayfirst = True)
CPRT_data.set_index(CPRT_data['Date'], inplace=True)
CPRT_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
CPRT_data.rename(columns={'Close': 'CPRT Close'}, inplace=True)
CMCSA_data['Date'] = pd.to_datetime(CMCSA_data["Date"], dayfirst = True)
CMCSA_data.set_index(CMCSA_data['Date'], inplace=True)
CMCSA_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
CMCSA_data.rename(columns={'Close': 'CMCSA Close'}, inplace=True)
CSCO_data['Date'] = pd.to_datetime(CSCO_data["Date"], dayfirst = True)
CSCO_data.set_index(CSCO_data['Date'], inplace=True)
CSCO_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
CSCO_data.rename(columns={'Close': 'CSCO Close'}, inplace=True)
TMUS_data['Date'] = pd.to_datetime(TMUS_data["Date"], dayfirst = True)
TMUS_data.set_index(TMUS_data['Date'], inplace=True)
TMUS_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
TMUS_data.rename(columns={'Close': 'TMUS Close'}, inplace=True)
AEP_data['Date'] = pd.to_datetime(AEP_data["Date"], dayfirst = True)
AEP_data.set_index(AEP_data['Date'], inplace=True)
AEP_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
AEP_data.rename(columns={'Close': 'AEP Close'}, inplace=True)
AAPL_data['Date'] = pd.to_datetime(AAPL_data["Date"], dayfirst = True)
AAPL_data.set_index(AAPL_data['Date'], inplace=True)
AAPL_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
AAPL_data.rename(columns={'Close': 'AAPL Close'}, inplace=True)
NVDA_data['Date'] = pd.to_datetime(NVDA_data["Date"], dayfirst = True)
NVDA_data.set_index(NVDA_data['Date'], inplace=True)
NVDA_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
NVDA_data.rename(columns={'Close': 'NVDA Close'}, inplace=True)
GOOG_data['Date'] = pd.to_datetime(GOOG_data["Date"], dayfirst = True)
GOOG_data.set_index(GOOG_data['Date'], inplace=True)
GOOG_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
GOOG_data.rename(columns={'Close': 'GOOG Close'}, inplace=True)
ODFL_data['Date'] = pd.to_datetime(ODFL_data["Date"], dayfirst = True)
ODFL_data.set_index(ODFL_data['Date'], inplace=True)
ODFL_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
ODFL_data.rename(columns={'Close': 'ODFL Close'}, inplace=True)
CSX_data['Date'] = pd.to_datetime(CSX_data["Date"], dayfirst = True)
CSX_data.set_index(CSX_data['Date'], inplace=True)
CSX_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
CSX_data.rename(columns={'Close': 'CSX Close'}, inplace=True)
HON_data['Date'] = pd.to_datetime(HON_data["Date"], dayfirst = True)
HON_data.set_index(HON_data['Date'], inplace=True)
HON_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
HON_data.rename(columns={'Close': 'HON Close'}, inplace=True)
MRNA_data['Date'] = pd.to_datetime(MRNA_data["Date"], dayfirst = True)
MRNA_data.set_index(MRNA_data['Date'], inplace=True)
MRNA_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
MRNA_data.rename(columns={'Close': 'MRNA Close'}, inplace=True)
AZN_data['Date'] = pd.to_datetime(AZN_data["Date"], dayfirst = True)
AZN_data.set_index(AZN_data['Date'], inplace=True)
AZN_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
AZN_data.rename(columns={'Close': 'AZN Close'}, inplace=True)
DXCM_data['Date'] = pd.to_datetime(DXCM_data["Date"], dayfirst = True)
DXCM_data.set_index(DXCM_data['Date'], inplace=True)
DXCM_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
DXCM_data.rename(columns={'Close': 'DXCM Close'}, inplace=True)
WBA_data['Date'] = pd.to_datetime(WBA_data["Date"], dayfirst = True)
WBA_data.set_index(WBA_data['Date'], inplace=True)
WBA_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
WBA_data.rename(columns={'Close': 'WBA Close'}, inplace=True)
KDP_data['Date'] = pd.to_datetime(KDP_data["Date"], dayfirst = True)
KDP_data.set_index(KDP_data['Date'], inplace=True)
KDP_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
KDP_data.rename(columns={'Close': 'KDP Close'}, inplace=True)
KHC_data['Date'] = pd.to_datetime(KHC_data["Date"], dayfirst = True)
KHC_data.set_index(KHC_data['Date'], inplace=True)
KHC_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
KHC_data.rename(columns={'Close': 'KHC Close'}, inplace=True)
DLTR_data['Date'] = pd.to_datetime(DLTR_data["Date"], dayfirst = True)
DLTR_data.set_index(DLTR_data['Date'], inplace=True)
DLTR_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
DLTR_data.rename(columns={'Close': 'DLTR Close'}, inplace=True)
MELI_data['Date'] = pd.to_datetime(MELI_data["Date"], dayfirst = True)
MELI_data.set_index(MELI_data['Date'], inplace=True)
MELI_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
MELI_data.rename(columns={'Close': 'MELI Close'}, inplace=True)
TSLA_data['Date'] = pd.to_datetime(TSLA_data["Date"], dayfirst = True)
TSLA_data.set_index(TSLA_data['Date'], inplace=True)
TSLA_data.drop(columns=['Date',"Adj Close","Open", "High", "Low", "Volume"],inplace=True)
TSLA_data.rename(columns={'Close': 'TSLA Close'}, inplace=True)

BM = pd.concat([FAST_data, CPRT_data, CMCSA_data], axis='columns', join='inner')
Tele = pd.concat([CSCO_data, TMUS_data, AEP_data], axis='columns', join='inner')
Disc = pd.concat([DLTR_data, MELI_data, TSLA_data], axis='columns', join='inner')
Stp = pd.concat([WBA_data, KDP_data, KHC_data], axis='columns', join='inner')
Health = pd.concat([MRNA_data, DXCM_data, AZN_data], axis='columns', join='inner')
Industrials = pd.concat([ODFL_data, CSX_data, HON_data], axis='columns', join='inner')
Tech = pd.concat([AAPL_data, NVDA_data, GOOG_data], axis='columns', join='inner')