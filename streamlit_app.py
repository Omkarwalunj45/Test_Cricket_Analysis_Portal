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

if pdf.empty:
    st.warning("The DataFrame is empty after loading!")
else:
    st.success("Data loaded successfully!")
    pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
    st.write(f"DataFrame shape: {pdf.shape}")  # Display the shape of the DataFrame
    st.write(pdf.tail())  # Display the first few rows of the DataFrame
bpdf=pdf
idf = pd.read_csv("Datasets/lifesaver_bat_tests.csv",low_memory=False)
bidf = pd.read_csv("Datasets/lifesaver_bowl_tests.csv",low_memory=False)
sidebar_option = st.sidebar.radio(
    "Select an option:",
    ("Player Profile", "Matchup Analysis","Strength vs Weakness","Match by Match Analysis")
)
