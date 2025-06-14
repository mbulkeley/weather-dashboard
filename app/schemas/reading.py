from pydantic import BaseModel
from datetime import datetime

class ReadingBase(BaseModel):
    temperature: float
    humidity: float
    station_id: int

class ReadingCreate(ReadingBase):
    pass

class ReadingOut(ReadingBase):
    id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }

