import streamlit as st
import pandas as pd
# write the title
st.title('The Best Company')
# write the company description
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat.
"""
# add company description
st.write(content)
st.header('Our Team')
# create columns
col1, col2, col3 = st.columns(3)
# read and store csv file
df = pd.read_csv('company_data.csv')

with col1:
    # iterate over rows 0 to 3
    for index, row in df[:4].iterrows():
        # create sub headers with full names
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        # write about roles
        st.write(row['role'])
        # create image
        st.image('company_imgs/'+row['image'])

with col2:
    # iterate over rows 4 to 8
    for index, row in df[4:8].iterrows():
        # create sub headers with full names
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        # write about roles
        st.write(row['role'])
        # create image
        st.image('company_imgs/'+row['image'])

with col3:
    # iterate over rows 8 to 12
    for index, row in df[8:].iterrows():
        # create sub headers with full names
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        # write about roles
        st.write(row['role'])
        # create image
        st.image('company_imgs/'+row['image'])

