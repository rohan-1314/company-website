import streamlit as st
import pandas as pd

st.title('The Best Company')
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat.
"""
st.write(content)
st.header('Our Team')
col1, col2, col3 = st.columns(3)
df = pd.read_csv('company_data.csv', sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'].capitalize() + " " + row['last name'].capitalize())

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())

with col3:
    for index, row in df[8:].iterrows():
        st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
