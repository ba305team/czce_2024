#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:37:02 2024

@author: zichengli
"""

import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load the data
dataframe = pd.read_csv('un_portwatch_suez.csv')

# Convert 'DateTime' column to datetime object
dataframe = dataframe.iloc[:,:5]
dataframe['DateTime'] = pd.to_datetime(dataframe['DateTime'])

# Set 'DateTime' as the index
dataframe.set_index('DateTime', inplace=True)

# Create the bar traces for cargo and tanker ships
trace1 = go.Bar(x=dataframe.index, y=dataframe['Number of Cargo Ships'], name='Number of Cargo Ships')
trace2 = go.Bar(x=dataframe.index, y=dataframe['Number of Tanker Ships'], name='Number of Tanker Ships')

# Create the line traces for the moving averages
trace3 = go.Scatter(x=dataframe.index, y=dataframe['7-day Moving Average'], mode='lines', name='7-day Moving Average')
trace4 = go.Scatter(x=dataframe.index, y=dataframe['Prior Year: 7-day Moving Average'], mode='lines', name='Prior Year: 7-day Moving Average')

# Combine all traces
data = [trace1, trace2, trace3, trace4]

# Create the layout
layout = go.Layout(
    title='Suez Canal Transit Tracking',
    barmode='group',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Transit Calls'),
    legend=dict(x=0, y=1.0)
)

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Display the figure in Streamlit
st.write('Suez Canal Transit Tracking')
st.plotly_chart(fig)

dataframe