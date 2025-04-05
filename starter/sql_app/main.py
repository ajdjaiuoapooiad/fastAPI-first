from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime
import requests
from .models import User, Room, Booking



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