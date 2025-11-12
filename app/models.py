from pydantic import BaseModel

class Character(BaseModel):
    id: int
    year: int
    name: str
    game: str
