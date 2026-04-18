from dataclasses import dataclass
from datetime import datetime

@dataclass
class GameModel:
    game_id: int
    name: str 
    price: float
    date: datetime
