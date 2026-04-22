import datetime as dt
import asyncio
import discord

from dotenv import load_dotenv
from os import getenv
from database.manager import DataBaseManager
from database.models import GameModel
from services.parser import Tracker
from services.graphs import Graph
from bot.client import SteamBot

load_dotenv()

user = getenv("USER")
password = getenv("PASSWORD")
token = getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True


async def start():
    db = await DataBaseManager.create(user, password)

    games_raw = await db.get_all_games()
    games = []

    for game_raw in games_raw:
        game = GameModel(**game_raw)
        games.append(game)

    async with SteamBot(database=db, intents=intents, command_prefix="!") as bot:
        await bot.start(token)
        await bot.setup_hook()


asyncio.run(start())