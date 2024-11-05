# import streamlit as st
# import pandas as pd
# import gdown
# import math as mt
# import numpy as np
# import matplotlib.pyplot as plt
# st.set_page_config(page_title='Test Cricket Performance Analysis Portal', layout='wide')
# st.title('Test Cricket Performance Analysis Portal')
# @st.cache_data
# def load_data():
#     """Load cricket data from Google Drive"""
#     try:
#         # Your Google Drive file ID
#         file_id = '1ljpdtij42aAkFEVsyTP6frkbt-A1oxgZ'
        
#         # Create the direct download link
#         download_link = f'https://drive.google.com/uc?id={file_id}'
        
#         # Download and read the file
#         output = 'cricket_data.csv'
#         gdown.download(download_link, output, quiet=False)
        
#         # Read the downloaded file
#         df = pd.read_csv(output)
#         return df
    
#     except Exception as e:
#         st.error(f"Error loading data: {str(e)}")
#         return None

# pdf=load_data()
# bpdf=pdf
# pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
# bpdf['legal_ball'] = bpdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
# @st.cache_data
# def load_bowling_data():
#     """Load bowling data from Google Drive"""
#     try:
#         # Your Google Drive file ID for bowling data
#         file_id = '1-En14nPHfxJoOKJJRv4dC1rX_9q_1QjY'
#         download_link = f'https://drive.google.com/uc?id={file_id}'
        
#         output = 'cricket_data.csv'
#         gdown.download(download_link, output, quiet=False)
        
#         df = pd.read_csv(output)
#         return df
    
#     except Exception as e:
#         st.error(f"Error loading bowling data: {str(e)}")
#         return None

# @st.cache_data
# def load_batting_data():
#     """Load batting data from Google Drive"""
#     try:
#         # Add your batting data file ID here
#         file_id = '1-9AGcGSaesnRhB-zySb1-_VdBfiElGCa'  # Replace with actual file ID for lifesaver_bat_tests.csv
#         download_link = f'https://drive.google.com/uc?id={file_id}'
        
#         output = 'batting_data.csv'
#         gdown.download(download_link, output, quiet=False)
        
#         return pd.read_csv(output)
    
#     except Exception as e:
#         st.error(f"Error loading batting data: {str(e)}")
#         return None
# idf=load_batting_data()
# bidf=load_bowling_data()

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
        file_id = '1ljpdtij42aAkFEVsyTP6frkbt-A1oxgZ'
        download_link = f'https://drive.google.com/uc?id={file_id}'
        output = 'cricket_data.csv'
        gdown.download(download_link, output, quiet=False)
        
        # Load CSV with low_memory=False to avoid dtype issues
        df = pd.read_csv(output, low_memory=False)
        return df
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

pdf = load_data()

# Ensure pdf is loaded successfully before modifying it
if pdf is not None:
    pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)

@st.cache_data
def load_bowling_data():
    """Load bowling data from Google Drive"""
    try:
        file_id = '1-En14nPHfxJoOKJJRv4dC1rX_9q_1QjY'
        download_link = f'https://drive.google.com/uc?id={file_id}'
        output = 'bowling_data.csv'  # Use a unique output file name
        gdown.download(download_link, output, quiet=False)
        
        df = pd.read_csv(output, low_memory=False)
        return df
    
    except Exception as e:
        st.error(f"Error loading bowling data: {str(e)}")
        return None

@st.cache_data
def load_batting_data():
    """Load batting data from Google Drive"""
    try:
        file_id = '1-9AGcGSaesnRhB-zySb1-_VdBfiElGCa'
        download_link = f'https://drive.google.com/uc?id={file_id}'
        output = 'batting_data.csv'  # Use a unique output file name
        gdown.download(download_link, output, quiet=False)
        
        df = pd.read_csv(output, low_memory=False)
        return df
    
    except Exception as e:
        st.error(f"Error loading batting data: {str(e)}")
        return None

idf = load_batting_data()
bidf = load_bowling_data()

if pdf is not None:
    st.write("Loaded main cricket data:")
    st.write(pdf.head())

if idf is not None:
    st.write("Loaded batting data:")
    st.write(idf.head())

if bidf is not None:
    st.write("Loaded bowling data:")
    st.write(bidf.head())

