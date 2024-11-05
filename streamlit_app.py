import streamlit as st
import pandas as pd
import math as mt
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title='Test Cricket Performance Analysis Portal', layout='wide')
st.title('Test Cricket Performance Analysis Portal')
# input_file = 'Datasets/tests_final.csv.xz'
# # Create a function to load and return the DataFrame
# # Load the compressed file with caching
# # df = st.cache_data(lambda: pd.read_csv(input_file, compression='xz', low_memory=False))()
# df = st.cache_data(pd.read_csv)(input_file, compression='xz', low_memory=False)
# # Now you can use df in your Streamlit app
# pdf=df
# pdf = pdf.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
# pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
# # st.write(pdf.tail())
def load_data(input_file):
    """
    Load and preprocess the data for a Streamlit app.
    
    Parameters:
    input_file (str): Path to the input CSV file (compressed with xz)
    
    Returns:
    pandas.DataFrame: The preprocessed DataFrame
    """
    # Load the compressed file with caching
    df = st.cache_data(pd.read_csv)(input_file, compression='xz', low_memory=False)
    
    # Drop unnecessary columns
    df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
    
    # Create a 'legal_ball' column based on the 'outcome' column
    df['legal_ball'] = df.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
    
    return df
pdf=load_data('Datasets/tests_final.csv.xz')
# pdf=merged_df
bpdf=pdf
idf = pd.read_csv("Datasets/lifesaver_bat_tests.csv",low_memory=False)
idf = idf.drop(columns=['Unnamed: 0'])
bidf = pd.read_csv("Datasets/lifesaver_bowl_tests.csv",low_memory=False)
st.switch_page("pages/Career Statistics.py")
