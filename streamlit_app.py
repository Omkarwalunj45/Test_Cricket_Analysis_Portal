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
    # st.success("Data loaded successfully!")
    pdf['legal_ball'] = pdf.apply(lambda row: 1 if row['outcome'] in ['no run', 'out', 'four', 'run', 'six', 'leg bye', 'bye'] else 0, axis=1)
    # st.write(f"DataFrame shape: {pdf.shape}")  # Display the shape of the DataFrame
    # st.write(pdf.tail())  # Display the first few rows of the DataFrame
bpdf=pdf
idf = pd.read_csv("Datasets/lifesaver_bat_tests.csv",low_memory=False)
bidf = pd.read_csv("Datasets/lifesaver_bowl_tests.csv",low_memory=False)
sidebar_option = st.sidebar.radio(
    "Select an option:",
    ("Player Profile", "Matchup Analysis","Strength vs Weakness","Match by Match Analysis")
)
if sidebar_option == "Player Profile":
    st.header("Player Profile")

    # Player search input (selectbox)
    player_name = st.selectbox("Search for a player", idf['batsman'].unique())

    # Filter the data for the selected player
    player_info = idf[idf['batsman'] == player_name].iloc[0]
    # Tabs for "Overview", "Career Statistics", and "Current Form"
    tab1, tab2 = st.tabs(["Career Statistics", "Current Form"])
    with tab2:
            st.header("Career Statistics")
    
            # Dropdown for Batting or Bowling selection
            option = st.selectbox("Select Career Stat Type", ("Batting", "Bowling"))
    
            # Show Career Averages based on the dropdown
            st.subheader("Career Performance")
    
            # Display Career Averages based on selection
            if option == "Batting":
                # Create a temporary DataFrame and filter the player's row
                temp_df = idf.drop(columns=['final_year'])
                player_stats = temp_df[temp_df['batsman'] == player_name]  # Filter for the selected player
    
                # Convert column names to uppercase and replace underscores with spaces
                player_stats.columns = [col.upper().replace('_', ' ') for col in player_stats.columns]
                player_stats=round_up_floats(player_stats)
                # Display the player's statistics in a table format with bold headers
                st.markdown("### Batting Statistics")
                columns_to_convert = ['RUNS','HUNDREDS', 'FIFTIES','THIRTIES', 'HIGHEST SCORE']
    
                   # Fill NaN values with 0
                player_stats[columns_to_convert] = player_stats[columns_to_convert].fillna(0)
                    
                   # Convert the specified columns to integer type
                player_stats[columns_to_convert] = player_stats[columns_to_convert].astype(int)
                # player_stats=player_stats.drop(columns={'UNNAMED:0'})
                st.table(player_stats.style.set_table_attributes("style='font-weight: bold;'"))                
                # Initializing an empty DataFrame for results and a counter
