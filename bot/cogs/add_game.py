import discord

from discord import app_commands
from discord.ext import commands
from services.parser import Tracker
from database.models import NewGameModel


class AddGame(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="add_game", description="Add a game to monitoring")
    @app_commands.describe(game_id="ID of game you want to start monitoring")
    async def add_game(self, ctx: commands.Context, game_id):
        await ctx.defer()
        game = await Tracker.create(game_id)
        text = discord.Embed(title=f"Игра {game.game_name} успешно добавлена!", description=f"Ценна на данный момент: {game.price}", color=discord.Colour.from_rgb(155, 33, 255))
        game_model = NewGameModel(game.game_id, game.game_name, game.price, game.date)
        try:
            await self.bot.database.add_game(game_model)
        except Exception as e:
            print(e)
        await ctx.send(embed=text)


async def setup_add_game(bot: commands.Bot):
    await bot.add_cog(AddGame(bot))
