import streamlit as st
import datetime 
import requests
import json
import pandas as pd
import random




page = st.sidebar.selectbox('Choose your page', ['users', 'rooms', 'bookings'])

if page == 'users':
    st.title("Booking System")

    with st.form(key='user'):
        user_id: int = random.randint(0, 10)
        username: str = st.text_input("Username", max_chars=50)
        data = {
            # 'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='Create User')
    
        if submit_button:
            st.write("User Created")
            st.json(data)
            st.write("User ID:", user_id)
            res = requests.post("http://localhost:8000/users", json=data)
            st.json(res.json())

if page == 'users':
    st.title("Booking System")

    with st.form(key='user'):
        user_id: int = random.randint(0, 10)
        username: str = st.text_input("Username", max_chars=50)
        data = {
            # 'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='Create User')
    
        if submit_button:
            st.write("User Created")
            st.json(data)
            st.write("User ID:", user_id)
            res = requests.post("http://localhost:8000/users", json=data)
            st.json(res.json())