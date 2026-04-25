import discord

from discord import app_commands
from discord.ext import commands
from services.graphs import Graph

class GetGraph(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="graph", description="Draw a graph of game")
    @app_commands.describe(game_id="Game ID to view its analytics graph.")
    async def graph(self, ctx: commands.Context, game_id):
        try:
            data = await self.bot.database.select(int(game_id), 7)
        except ValueError:
            text = discord.Embed(title="Error", description="Something wrong", color=discord.Colour.from_rgb(155, 33, 255))
            await ctx.send(embed=text, file=image)
        try:
            if not data[0].price:
                text = discord.Embed(title="Game not in database!", description="Price of game:", color=discord.Colour.from_rgb(255, 213, 0))
                await ctx.send(embed=text)
            else:
                graph = await Graph.create(data)
                image_name = graph.save_graph()
                image = discord.File(image_name)
                text = discord.Embed(title="Graph for 7 days", description="Data prices of game for last 7 days", color=discord.Colour.from_rgb(155, 33, 255))
                text.set_image(url=f"attachment://{image.filename}")
                
                await ctx.send(embed=text, file=image)
        except Exception as e: print(e)

async def setup_get_graph(bot: commands.Bot):
    await bot.add_cog(GetGraph(bot))
