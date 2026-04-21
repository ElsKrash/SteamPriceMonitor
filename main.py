import datetime as dt
import asyncio

from dotenv import load_dotenv
from os import getenv
from database.manager import DataBaseManager
from database.models import GameModel
from services.parser import Tracker
from services.graphs import Graph

load_dotenv()

user = getenv("USER")
password = getenv("PASSWORD")

async def start():
    database = await DataBaseManager.create(user, password)

    games_raw = await database.get_all_games()
    games = []

    for game_raw in games_raw:
        game = GameModel(**game_raw)
        games.append(game)

    print(games)


asyncio.run(start())