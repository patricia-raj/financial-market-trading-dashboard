# Financial Market Trading Dashboard

Create a streamlit application with multiple pages containing key information necessary to a trader / investor to make informed decision for investment.

## Details

1) A index & the sector based chart across different timelines to get a macro view.
![](Images/Indices.mp4)

https://user-images.githubusercontent.com/99471693/183242482-a244fd3b-bbc6-441f-9b7a-2982b182abab.mp4



https://user-images.githubusercontent.com/99471693/183242490-d94f01d9-2497-4e97-b9c0-1955778f170a.mp4




![](Images/Sector.mp4)

2) A stock screener like in yahoo finance (we want to limit the pool to nasdaq 100 for simplicity).
![](Images/Screener.mp4)


https://user-images.githubusercontent.com/99471693/183242500-47b91718-d089-4d24-908b-a9bc75825740.mp4




3) Real time deeper lens to analyse stock Financials and returns.
![](Images/Stock_Financials.mp4)


https://user-images.githubusercontent.com/99471693/183242508-c861ab3d-3f41-4fd1-b79e-25510e0f6a56.mp4


![](Images/Stock_Price.mp4)


https://user-images.githubusercontent.com/99471693/183242515-8e12b0fa-5d42-4e63-a6d9-c889dca32d63.mp4



4) An algo back testing feature that can run on the above pool of stocks with customizable dates.

![](Images/Algo_Trading.png)

## Summary
- We pushed our ability to do real-time integration with Yfinance to provide traders closer real-time experience.

- Lot of challenges in understanding YFinance API in short time and necessiated many pre-processing steps to handle unavailability of data.

- Near real time comparison US region major indicies and across other regions was profound for predictions.

- With less exposure building streamlit application, we are happy to integrate the stock key information and visualization using interactive user experience.

- As icing on the top, Dual moving average crossover trading Algorithm strategy was implemented to visualize profit and loss along with ROI.


## Collaborators

* **Alyssa Younger** 
* **John Ryan** 
* **Kamalnivas Balasubramanian** 
* **Patricia Rajamanickam** 


## Installation Guide
- #### Must have Anaconda base ####

```
conda activate base
conda create -n project3streamlitenv python=3.7 -y
conda activate project3streamlitenv
conda install -c pyviz holoviz -y
conda install -c conda-forge yfinance -y
conda install -c conda-forge html5lib -y
conda install -c conda-forge streamlit -y
conda install -c conda-forge jupyterlab -y
conda install -c conda-forge hvplot -y
conda install -c conda-forge matplotlib -y
conda install -c conda-forge plotly -y
conda install -c conda-forge nodejs -y
conda install -c conda-forge bokeh==2.4.3 -y
conda install -c conda-forge panel -y

```

## Project Presentation
[Project3.pptx](https://github.com/patricia-raj/financial-market-trading-dashboard/files/9275495/Project3.pptx)
