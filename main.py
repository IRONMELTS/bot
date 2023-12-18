import discord
import os
from discord.ext import commands

intents=discord.Intents.all()

bot=commands.Bot(command_prefix='.',intents=intents)

@bot.event
async def on_ready():
    print("BOT is ready")
    status=discord.Game(name="sleeping")
    await bot.change_presence(status=discord.Status.idle,activity=status)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")

bot.run(os.environ["token"])
