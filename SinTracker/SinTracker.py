import os

from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

from database_setup import initialize_db

load_dotenv()
TOKEN = os.getenv('SIN_TRACKER_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=["$","Sin", "SIN", "sin"], intents=intents)

@bot.event
async def on_ready():
    try:
        initialize_db()
    except Exception as e:
        print(f"Failed to initialize database: {e}")
        await bot.close()
        return

    await bot.tree.sync()
    print(f'Bot is online as {bot.user}')

@bot.tree.command(name="help", description="Shows all available commands")
async def help_command(interaction: discord.Interaction):
    # Build a list of all registered slash commands excluding this (help).
    commands_list = [
        f"/{cmd.name} - {cmd.description}" 
        for cmd in bot.tree.get_commands()
        if cmd.name != "help"
    ]
    
    await interaction.response.send_message(
        "\nHere are my commands:\n" + "\n".join(commands_list),
        ephemeral=True
    )

@bot.tree.command(name="sinners", description="Shows the names of the Sinners!")
async def sinners_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Coonah the Cuck\nPat O'Well the Smell\nRupert the Bear with the fear of a Bare Pair\nWazzy the Wonderful",
        ephemeral=True
    )

@bot.tree.command(name="total-sins", description="Shows the total number of Sins accumulated by the Sinners!")
async def totalSins_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Total: TBC",
        ephemeral=True
    )

bot.run(TOKEN)