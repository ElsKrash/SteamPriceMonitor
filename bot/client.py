import discord

from discord import app_commands
from discord.ext import commands
from bot.cogs.get_graph import setup_get_graph
from bot.cogs.add_game import setup_add_game
from database.manager import DataBaseManager


class SteamBot(commands.Bot):
    def __init__(self, database, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database: DataBaseManager = database

    
    async def setup_hook(self):
        await setup_add_game(self)
        await setup_get_graph(self)

        await self.tree.sync()
        print("Команды синхронизированы!")