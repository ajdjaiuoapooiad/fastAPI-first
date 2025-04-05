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




elif page == 'rooms':
    st.title('会議室登録画面')

    with st.form(key='room'):
        room_id: int = random.randint(0, 10)
        room_name: str = st.text_input('会議室名', max_chars=12)
        capacity: int = st.number_input('定員', step=1)
        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='会議室登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('会議室登録完了')
        st.json(res.json())




elif page == 'bookings':
    st.title('予約登録画面')

    with st.form(key='booking'):
        booking_id: int = random.randint(0, 10)
        user_id: int = random.randint(0, 10)
        room_id: int = random.randint(0, 10)
        booked_num: int = random.randint(0, 10)
        start_datetime: datetime.datetime = st.date_input('開始日時', datetime.datetime.now())
        end_datetime: datetime.datetime = st.date_input('終了日時', datetime.datetime.now())
        
        data = {
            'booking_id': booking_id,
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': start_datetime.isoformat(),
            'end_datetime': end_datetime.isoformat()
        }
        submit_button = st.form_submit_button(label='予約登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/bookings'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('予約登録完了')
        st.json(res.json())
