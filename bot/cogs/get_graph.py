import discord

from discord import app_commands
from discord.ext import commands


class GetGraph(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="graph", description="Draw a graph of game")
    async def graph(self, ctx: commands.Context):
        image = discord.File("graph.jpg")
        text = discord.Embed(title="График цен за 7 дней", description="Данные по ценам на игру за последние 7 дней", color=discord.Colour.from_rgb(155, 33, 255))
        text.set_image(url="attachment://graph.jpg")
        await ctx.send(embed=text, file=image)

async def setup_get_graph(bot: commands.Bot):
    await bot.add_cog(GetGraph(bot))
