# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px
import plotly.io as pio
pio.templates.default='seaborn'

# Add title Part 1A and 1B
st.title("Project Part 1A")

# Define the columns you want to use 
columns_to_use = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type', 'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales']

# Function for loading data
# Adding data caching
@st.cache_data
def load_data():
    fpath =  "Data/item_fat_content.csv"
    df = pd.read_csv(fpath)
    df = df[columns_to_use]
    return df

# load the data 
df = load_data()

# Display an interactive dataframe
st.header("Product Sales Data")
st.dataframe(df, width=800)

# Display descriptive statistics
st.markdown('#### Descriptive Statistics')
st.dataframe(df.describe().round(2))

from io import StringIO
# Create a string buffer to capture the content
buffer = StringIO()
# Write the info into the buffer
df.info(buf=buffer)
# Retrieve the content from the buffer
summary_info = buffer.getvalue()
# Display Information

if st.button('#### Information'):
    st.text(summary_info)

# We could display the output series as a dataframe
st.markdown("#### Null Values")
nulls =df.isna().sum()
st.dataframe(nulls)
