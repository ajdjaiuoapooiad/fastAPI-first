from fastapi import FastAPI
from pydantic import BaseModel, fields
from datetime import datetime

class Booking(BaseModel):
    booking_id = int
    user_id =  int
    room_id = int 
    booked_num = int
    start_datetime = datetime.datetime
    end_datetime = datetime.datetime

class User(BaseModel):
    user_id = int
    username = fields("username", max_length=50)

class Room(BaseModel):
    room_id = int
    room_name = fields("room_name", max_length=50)
    capacity = int


app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, World!"}

@app.post("/users")
async def index(users: User):
    return {"users":users}

@app.post("/rooms")
async def index(room: Room):
    return {"rooms": room}

@app.post("/bookings")
async def index(booking: Booking):
    return {"bookings": booking}