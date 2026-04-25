from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class GameModel:
    game_id: int
    name: str 
    date: datetime
    price: Optional[float] = None

@dataclass
class PricePoint:
    price: float
    date: datetime
