import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config('wide')

df = pd.read_csv('india_census.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Selec a State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('color represent secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=3, size=primary, color=Secondary, mapbox_style='carto-positron', hover_name='District')
        st.plotly_chart(fig, use_container_width=True)

    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=3, size=primary, color=Secondary, mapbox_style='carto-positron', hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
