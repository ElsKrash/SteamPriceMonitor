import datetime as dt
import asyncio

from dotenv import load_dotenv
from os import getenv
from database.manager import DataBaseManager

load_dotenv()

user = getenv("user")
password = getenv("password")

async def start():
    database = await DataBaseManager.create(user, password)
    await database.add_game(125, "Test", dt.datetime.now())

asyncio.run(start())