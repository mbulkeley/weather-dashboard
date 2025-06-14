from pydantic import BaseModel

class StationBase(BaseModel):
    name: str
    location: str

class StationCreate(StationBase):
    pass

class StationOut(StationBase):
    id: int

    model_config = {
        "from_attributes": True
    }
