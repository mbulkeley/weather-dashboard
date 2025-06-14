from fastapi import FastAPI
from app.db import models
from app.db.session import engine, Base
from app.api.v1 import readings
from fastapi.middleware.cors import CORSMiddleware
from app.db.seed import seed_stations

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Frontend container
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
seed_stations()

from app.db.session import SessionLocal
from app.db.models import Station
from app.api.v1 import readings, stations 

# TEMP: create a default station if not exists
with SessionLocal() as db:
    if not db.query(Station).filter_by(name="Test Station").first():
        default_station = Station(name="Test Station", location="Test Lab")
        db.add(default_station)
        db.commit()

app.include_router(readings.router)  # 👈 mount the readings routes
app.include_router(stations.router)

@app.get("/")
def root():
    return {"message": "Welcome to Weather Dashboard!"}
