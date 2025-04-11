from pydantic import BaseModel

class TableSchema(BaseModel):
    id : int
    name: str
    seats : int
    location : str

    class Config:
        from_attributes = True

class TableSchemaAdd(BaseModel):
    name: str
    seats : int
    location : str