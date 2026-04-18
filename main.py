import datetime as dt
import asyncio

from dotenv import load_dotenv
from os import getenv
from database.manager import DataBaseManager
from database.models import GameModel
from services.parser import Tracker
from services.graphs import Graph

load_dotenv()

user = getenv("user")
password = getenv("password")

async def start():
    database = await DataBaseManager.create(user, password)

    game = await Tracker.create(105600)
    
    game_data = GameModel(int(game.game_id), game.game_name, float(game.price), game.date)


    data = await database.select(game_data)

    graph = await Graph.create(data)
    graph.save_graph

asyncio.run(start())