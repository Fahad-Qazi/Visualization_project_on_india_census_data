import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

# our dataframe
df = pd.read_csv(r'c:\Users\Admin\OneDrive\Desktop\100_Days_of_ML\04_Plotly\plotly_project\india-census-data.csv')

# all states list
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India Population Visualization")

selected_state = st.sidebar.selectbox('Select State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[6:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[6:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    # plot for overall india
    if plot:
        st.subheader("Insights")
        st.markdown(f"**Selected State:** {selected_state}")
        st.markdown(f"- **Primary Parameter:** {primary}")
        st.markdown(f"- **Secondary Parameter:** {secondary}")
        st.markdown("This scatter map represents the census data. Larger circles signify higher values of the primary parameter, "
                    "and the color scale represents variations in the secondary parameter.")
        
        
    # st.text('size represent primary parameter')
    # st.text('color represent secondary paramter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, size_max=20, zoom=3, 
                                mapbox_style="carto-positron", width=1600, height=600, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for states
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, size_max=20, zoom=5, 
                                mapbox_style="carto-positron", width=1600, height=600, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)


		
