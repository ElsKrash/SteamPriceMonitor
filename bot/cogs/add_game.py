import discord

from discord import app_commands
from discord.ext import commands
from services.parser import Tracker
from database.models import GameModel
from asyncpg import UniqueViolationError

class AddGame(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="add_game", description="Add a game to monitoring")
    @app_commands.describe(game_id="ID of game you want to start monitoring")
    async def add_game(self, ctx: commands.Context, game_id):
        await ctx.defer()
        game = await Tracker.create(game_id)
        game_model = GameModel(game.game_id, game.game_name, game.date, game.price)
        try:
            text = discord.Embed(title=f"Game {game.game_name} succesful added!", description=f"Price for now: {game.price}", color=discord.Colour.from_rgb(155, 33, 255))
            await self.bot.database.add_game(game_model)
            await ctx.send(embed=text)
        except UniqueViolationError:
            text = discord.Embed(title=f"Game {game.game_name} is already in database!", description=f"For check price use /graph!", color=discord.Colour.from_rgb(252, 3, 3))
            await ctx.send(embed=text)


async def setup_add_game(bot: commands.Bot):
    await bot.add_cog(AddGame(bot))
