import streamlit as st
import pandas as pd
import gdown

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
