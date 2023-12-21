import discord
import time
import os
from discord.ext import commands

intents=discord.Intents.all()

bot=commands.Bot(command_prefix='.',intents=intents)

reply_id={}

@bot.event

async def on_ready():

    print("BOT is ready")
    await bot.change_presence(activity=discord.Game(name="~~~ready~~~"))
    time.sleep(3)
    await bot.change_presence(activity=discord.Game(name=".help"))

    
@bot.command(name="ping")

async def ping(ctx):

    await ctx.send(f"{round(bot.latency*1000)}ms")

@bot.command(name="user")

async def user(ctx,user_id:int):

    user=await bot.fetch_user(user_id)
    await ctx.send(f"Account name: `{user.name}`\nAccount created on: `{str(user.created_at)[0:-13]}`")

@bot.command(name="av")

async def av(ctx,user_id:int):

    user=await bot.fetch_user(user_id)
    await ctx.send(user.avatar)
    
bot.run(os.environ["token"])
