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

# Use plotly for explore functions
def plotly_explore_numeric(df, x):
    fig = px.histogram(df,x=x,marginal='box',title=f'Distribution of {x}', 
                      width=1000, height=500)
    return fig
def plotly_explore_categorical(df, x):
    fig = px.histogram(df,x=x,color=x,title=f'Distribution of {x}', 
                          width=1000, height=500)
    fig.update_layout(showlegend=False)
    return fig
# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    fig = plotly_explore_categorical(df, column)
else:
    fig = plotly_explore_numeric(df, column)
    
st.markdown("#### Displaying appropriate Plotly plot based on selected column")
# Display appropriate eda plots
st.plotly_chart(fig)

# Add title
st.title("Project 1 Part 1B")

# Define the columns you want to use 
columns_to_use = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type', 'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales']
# Function for loading data
# Adding data caching
@st.cache_data
def load_data():
        fpath = "Data/item_fat_content.csv"
    df = pd.read_csv(fpath)
    df = df.set_index("PID")
    df = df[columns_to_use]
    return df

# load the data 
df = load_data()


##########################################################################################################################
# Solution to Plotly Practice Assignment

st.markdown("#### Explore Features vs. Target Plots with Plotly")
# Add a selectbox for all possible features (exclude SalePrice)
# Copy list of columns
features_to_use = columns_to_use[:]
# Define target
target = 'Item_Type'
# Remove target from list of features
features_to_use.remove(target)

# Add a selectbox for all possible columns
feature = st.selectbox(label="Select a feature to compare with Item_Type", options=features_to_use)



def plotly_numeric_vs_target(df, x, y='Item_Type', trendline='ols',add_hoverdata=True):
    if add_hoverdata == True:
        hover_data = list(df.columns)
    else: 
        hover_data = None
        
    pfig = px.scatter(df, x=x, y=y,width=800, height=600,
                     hover_data=hover_data,
                      trendline=trendline,
                      trendline_color_override='red',
                     title=f"{x} vs. {y}")
    
    pfig.update_traces(marker=dict(size=3),
                      line=dict(dash='dash'))
    return pfig

def plotly_categorical_vs_target(df, x, y='Item_Type', histfunc='avg', width=800,height=500):
    fig = px.histogram(df, x=x,y=y, color=x, width=width, height=height,
                       histfunc=histfunc, title=f'Compare {histfunc.title()} {y} by {x}')
    fig.update_layout(showlegend=False)
    return fig

# Conditional statement to determine which function to use
if df[feature].dtype == 'object':
    fig_vs  = plotly_categorical_vs_target(df, x = feature)
else:
    fig_vs  = plotly_numeric_vs_target(df, x = feature)

st.plotly_chart(fig_vs)