# app/api/v1/readings.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import models
from app.schemas.reading import ReadingCreate, ReadingOut

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/readings", response_model=ReadingOut)
def create_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    station = db.query(models.Station).filter(models.Station.id == reading.station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")

    db_reading = models.Reading(**reading.model_dump())

    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

@router.get("/readings", response_model=list[ReadingOut])
def get_readings(limit: int = 10, db: Session = Depends(get_db)):
    readings = (
        db.query(models.Reading)
        .order_by(models.Reading.timestamp.desc())
        .limit(limit)
        .all()
    )
    return readings
