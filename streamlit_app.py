import streamlit as st
import pandas as pd
import gdown
import math as mt
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title='Test Cricket Performance Analysis Portal', layout='wide')
st.title('Test Cricket Performance Analysis Portal')
@st.cache_data
def load_data():
    """Load cricket data from Google Drive"""
    try:
        # Your Google Drive file ID
        file_id = '1ljpdtij42aAkFEVsyTP6frkbt-A1oxgZ'
        
        # Create the direct download link
        download_link = f'https://drive.google.com/uc?id={file_id}'
        
        # Download and read the file
        output = 'cricket_data.csv'
        gdown.download(download_link, output, quiet=False)
        
        # Read the downloaded file
        df = pd.read_csv(output)
        return df
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

pdf=load_data()
bpdf=pdf
idf=pd.read_csv('Dataset/lifesaver_bat_tests.csv')
bidf=pd.read_csv('Dataset/lifesaver_bat_tests.csv')
pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
bpdf['legal_ball'] = bpdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)


