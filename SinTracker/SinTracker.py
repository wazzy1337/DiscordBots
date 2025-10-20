import os

from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('SIN_TRACKER_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=["$","Sin", "SIN", "sin"], intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def TotalSins(ctx):
    await ctx.send("Total:")

bot.run(TOKEN)