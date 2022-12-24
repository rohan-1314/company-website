import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv('topics.csv')

with st.form(key='form'):
    user_email = st.text_input(label='Your Email:')
    topic = st.selectbox('What topic do you want to discuss:', df['topic'])
    raw_message = st.text_area('Text:')
    message = f"""\
subject:new email from {user_email} 

from:{user_email}
topic: {topic}
{raw_message}
"""
    submit = st.form_submit_button('submit')
    if submit:
        send_email(message)
        st.info('Your email was sent successfully.')
