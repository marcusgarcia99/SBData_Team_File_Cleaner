import streamlit as st
import pandas as pd
import numpy as np
import re

st.title('File Cleaner: For Data Team')



col_1, col_2 = st.columns(spec=2, gap="medium", vertical_alignment="center")

def file_cleaner(df):
    data_copy = df.copy()

    column_names = data_copy.columns.values.tolist()

    new_column_names = []

    ind = 0

    for i in column_names:
        result = re.match(r'Unnamed: \d{2}',i)

        if result != None:
            new_column_names.append(new_column_names[-1])
            ind = ind + 1

        else:
            new_column_names.append(i)
            ind = ind + 1

    data_copy.columns = new_column_names
    data_copy = data_copy.drop(data.index[0])

    variable_list = new_column_names[0:9]

    data_copy = pd.melt(data_copy, id_vars= variable_list, var_name='Question', value_name= 'Response')

    data_copy = data_copy.drop_duplicates()


with col_1:
    st.write('Please upload file!')
    raw_file = st.file_uploader('Survey Data', type=['xlsx','csv'],key='uploaded_file')

with col_2:
    if raw_file not in st.session_state:
        st.write()
    else:
        st.write('Please wait while file cleaning is in progress!')

        clean_file = file_cleaner(raw_file)

        st.download_button('Clean File Complete',data= clean_file , file_name='Cleaned_File.csv')


st.markdown("""
<iframe width="560" height="315" 
src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1&loop=1&playlist=dQw4w9WgXcQ" 
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)
            

st.markdown("""
<iframe width="560" height="315" 
src="https://www.youtube.com/embed/jane6C4rIwc?autoplay=1&mute=1&loop=1&playlist=jane6C4rIwc" 
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)


#st.video('https://www.youtube.com/watch?v=mKdHMJtMNzQ')