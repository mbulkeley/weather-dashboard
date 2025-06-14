from app.db.session import SessionLocal
from app.db.models import Station

def seed_stations():
    db = SessionLocal()
    existing = db.query(Station).count()
    if existing == 0:
        stations = [
            Station(name="Garage Pi", location="Backyard"),
            Station(name="Office Sensor", location="Upstairs Office"),
            Station(name="Greenhouse Monitor", location="Garden Shed"),
        ]
        db.add_all(stations)
        db.commit()
        print("🌱 Seeded initial stations.")
    else:
        print("✅ Stations already seeded.")
    db.close()
