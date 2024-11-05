import streamlit as st
import pandas as pd
import gdown
import math as mt
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title='Test Cricket Performance Analysis Portal', layout='wide')
st.title('Test Cricket Performance Analysis Portal')
# url = 'https://drive.google.com/uc?id=1ljpdtij42aAkFEVsyTP6frkbt-A1oxgZ'  # Replace with your modified link
import gdown

# Google Drive file ID
file_id = '1ljpdtij42aAkFEVsyTP6frkbt-A1oxgZ'
download_link = f'https://drive.google.com/uc?id={file_id}'
output = 'cricket_data.csv'

gdown.download(download_link, output, quiet=False)

# Now read the downloaded CSV
pdf = pd.read_csv(output)

if df.empty:
    st.warning("The DataFrame is empty after loading!")
else:
    st.success("Data loaded successfully!")
    st.write(f"DataFrame shape: {df.shape}")  # Display the shape of the DataFrame
    st.write(df.head())  # Display the first few rows of the DataFrame

# pdf = pd.read_csv(url)
bpdf=pdf
# @st.cache_data
# def load_bowling_data():
#     """Load bowling data from Google Drive"""
#     try:
#         file_id = '1-KPeLgLYKT2-EaxtN2EUtRR2Q1JSinqe'
#         download_link = f'https://drive.google.com/uc?id={file_id}'
#         output = 'bowling_data.csv'  # Use a unique output file name
#         gdown.download(download_link, output, quiet=False)
        
#         df = pd.read_csv(output, low_memory=False)
#         return df
    
#     except Exception as e:
#         st.error(f"Error loading bowling data: {str(e)}")
#         return None
# bidf = load_bowling_data()
# @st.cache_data
# def load_batting_data():
#     """Load batting data from Google Drive"""
#     try:
#         file_id = '1-Oxw0ZiXT40k1VC0PUgrn_JyAjCCra5D'
#         download_link = f'https://drive.google.com/uc?id={file_id}'
#         output = 'batting_data.csv'  # Use a unique output file name
#         gdown.download(download_link, output, quiet=False)
        
#         df = pd.read_csv(output, low_memory=False)
#         return df
    
#     except Exception as e:
#         st.error(f"Error loading batting data: {str(e)}")
#         return None

idf = pd.read_csv("Datasets/lifesaver_bat_tests.csv",low_memory=False)
bidf = pd.read_csv("Datasets/lifesaver_bowl_tests.csv",low_memory=False)
# idf = load_batting_data()
st.write(pdf.head())
st.write(idf.head())
sidebar_option = st.sidebar.radio(
    "Select an option:",
    ("Player Profile", "Matchup Analysis","Strength vs Weakness","Match by Match Analysis")
)
