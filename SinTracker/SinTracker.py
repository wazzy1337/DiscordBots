import os

from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

from database import get_sins, get_total_sins, get_total_sins_by_player, initialize_db

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

@bot.tree.command(name="sins", description="Shows all the Sins the Sinners can commit!")
@app_commands.describe(cost="When true, retrieves sin amount instead of description (optional)")
async def sins_command(interaction: discord.Interaction, cost: bool = False):
    rows = get_sins()
    if not rows:
        await interaction.response.send_message("No sins found in the database.", ephemeral=True)
        return

    if cost:
        # Build a string listing all sins with their cost.
        # Use singular "Sin" if the count is 1, otherwise use plural "Sins".
        sins_list = "\n".join([
            f"**{row[0]}** = {row[2]} {'Sin' if row[2] == 1 else 'Sins'}"
            for row in rows
        ])
    else:
        sins_list = "\n".join([f"**{row[0]}** - {row[1]}" for row in rows])

    await interaction.response.send_message(f"Here are the sins:\n{sins_list}", ephemeral=True)

@bot.tree.command(name="sinners", description="Shows the names of the Sinners!")
async def sinners_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Coonah the Cuck\nPat O'Well the Smell\nRupert the Bear with the fear of a Bare Pair\nWazzy the Wonderful",
        ephemeral=True
    )

@bot.tree.command(name="total-sins", description="Shows the total number of Sins — optionally for a specific Sinner.")
@app_commands.describe(player="Name of the Sinner (optional, case-sensitive)")
async def total_sins_command(interaction: discord.Interaction, player: str = None):
    if player:
        total = get_total_sins_by_player(player)
        if total is None:
            msg = f"😈 No Sinner found with the name **{player}**"
        else:
            msg = f"**Total Sins 🐍:** {total} ({player})"
    else:
        total = get_total_sins()
        msg = f"**Total Sins 🐍:** {total} (All Sinners)"

    await interaction.response.send_message(msg, ephemeral=True)

@bot.tree.command(name="add-sin", description="Adds a Sin to a certain Sinner!")
@app_commands.describe(player="The sinner to add the sin to", sin="The sin being committed")
@app_commands.choices(
    player=[
        app_commands.Choice(name="Coonah the Cuck", value="Conner"),
        app_commands.Choice(name="Pat O'Well the Smell", value="Pat"),
        app_commands.Choice(name="Rupert the Bear", value="Rupert"),
        app_commands.Choice(name="Wazzy the Wonderful", value="Wazzy")
    ]
)
async def add_sin_command(interaction: discord.Interaction, player: app_commands.Choice[str], sin: str):
    await interaction.response.send_message(
        f"✅ **{player.name}** has been punished for **{sin}**! Sin recorded successfully.",
        ephemeral=True
    )

bot.run(TOKEN)