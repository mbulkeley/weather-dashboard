from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.station import StationCreate, StationOut
from app.db import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/stations", response_model=StationOut)
def create_station(station: StationCreate, db: Session = Depends(get_db)):
    db_station = models.Station(**station.model_dump())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

@router.get("/stations", response_model=list[StationOut])
def list_stations(db: Session = Depends(get_db)):
    return db.query(models.Station).all()
