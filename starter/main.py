from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime
import requests

class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class User(BaseModel):
    user_id: int
    username: str = Field(..., max_length=50)  # ... は必須フィールドを示す

class Room(BaseModel):
    room_id: int
    room_name: str = Field(..., max_length=50)  # ... は必須フィールドを示す
    capacity: int


app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, World!"}

@app.post("/users")
async def create_user(user: User):
    return {"user": user}

@app.post("/rooms")
async def create_room(room: Room):
    return {"room": room}

@app.post("/bookings")
async def create_booking(booking: Booking):
    return {"booking": booking}