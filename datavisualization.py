import pandas as pd
import streamlit as st
import plotly.express as px


st.subheader('📊 Simple Data Analyzer and Visualizer' )
uploaded_file = st.file_uploader(label = 'Choose a CSV File', type = 'csv') 

cont1 = st.container()
cont2 = st.container()


with cont1:
     if uploaded_file is not None:
          global dataframe
          dataframe = pd.read_csv(uploaded_file).dropna(axis = 'index', how = 'all')
          st.write(dataframe)                     

          st.subheader('Delete Unwanted Columns and Rows')
          st.markdown('📍  `You can skip this if your data is cleaned already.`')
          col = st.multiselect('Choose Columns to Delete', options = dataframe.columns)
          x = st.button('🗑️ Delete Columns', on_click = dataframe.drop( col,axis='columns', inplace=True))
          

          if x:
               try:
                    st.write(pd.DataFrame(data = dataframe))
               except Exception as e:
                    print(e)

          row = st.multiselect('Choose Rows to Delete', options = dataframe.index)
          y = st.button('🗑️ Delete Rows', on_click = dataframe.drop( row ,axis='index', inplace=True))

          if y:
               try:
                    st.write(pd.DataFrame(data = dataframe))
               except Exception as e:
                    print(e)

          with cont2:
               st.subheader('Select Plot Type')
               ha_1 = ['Scatter Plots', 'Line Plots', 'Bar Plots']
               sb = st.selectbox(label = 'Select the chart type', options = ha_1)
               if sb == 'Scatter Plots':
                    st.subheader("Settings")
                    col1, col2 = st.columns(2)
                    with col1:         
                         x_val = st.selectbox('X_axis', options = dataframe.columns)
                    with col2:
                         y_val = st.selectbox('Y_axis', options = dataframe.columns)
                    plot = px.scatter(data_frame = dataframe, x = x_val, y = y_val)
                    st.plotly_chart(plot)

               if sb == 'Line Plots':
                    st.subheader("Settings")
                    col3, col4 = st.columns(2)
                    with col3:         
                         x_val = st.selectbox('X_axis', options = dataframe.columns)
                    with col4:
                         y_val = st.selectbox('Y_axis', options = dataframe.columns)
                    plot = px.line(data_frame = dataframe, x = x_val, y = y_val, title = 'Line Graph')
                    st.plotly_chart(plot)

               if sb == 'Bar Plots':
                    st.subheader("Settings")
                    col5, col6 = st.columns(2)
                    with col5:         
                         x_val = st.selectbox('X_axis', options = dataframe.columns)
                    with col6:
                         y_val = st.selectbox('Y_axis', options = dataframe.columns)
                    plot = px.bar(data_frame = dataframe, x = x_val, y = y_val)
                    st.plotly_chart(plot)

               