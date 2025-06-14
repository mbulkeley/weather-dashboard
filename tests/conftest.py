import pytest
from app.db.session import SessionLocal
from app.db.models import Station, Reading

@pytest.fixture(autouse=True)
def clean_db():
    db = SessionLocal()
    db.query(Reading).delete()
    db.query(Station).delete()
    db.commit()
    db.close()
