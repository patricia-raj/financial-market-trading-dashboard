# Financial Market Trading Dashboard

Create a streamlit application with multiple pages of what might be useful to a trader / investor.

Currently, we plan to have the following:

- A index & the sector based chart across different timelines to get a macro view.

- A stock screener like in yahoo finance (we want to limit the pool to nasdaq 100 for simplicity).

- An algo back testing feature that can run on the above pool of stocks with customizable dates.

## Collaborators

|  | 
| ----------- | 
| * **Alyssa Younger** | 
| * **John Ryan** | 
| * **Kamalnivas Balasubramanian** | 
| * **Patricia Rajamanickam** | 

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