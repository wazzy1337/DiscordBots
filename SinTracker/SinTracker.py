import os

from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

from database import add_sin_to_player, get_sins, get_total_sins, get_total_sins_by_player, initialize_db
from Helpers.helper import build_sin_summary_description

load_dotenv()
TOKEN = os.getenv('SIN_TRACKER_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=["$","Sin", "SIN", "sin"], intents=intents)

channel_id = int(os.getenv("SINS_CHANNEL_ID"))

SINS = get_sins()
SIN_NAMES = [app_commands.Choice(name=sin[0], value=sin[0]) for sin in SINS]

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

    await post_sin_summary()

async def post_sin_summary():
    try:
        channel = bot.get_channel(channel_id)
        if channel is None:
            channel = await bot.fetch_channel(channel_id) #Covering a cold cache scenario.

        if channel is not None:
            # Check for existing Sin Summary message
            async for msg in channel.history(limit=100):
                if msg.author == channel.guild.me and msg.embeds:
                    if msg.embeds[0].title == "Sin Summary":
                        summary_message_id = msg.id
                        break

            sin_summary_description = build_sin_summary_description(["Conner", "Pat", "Rupert", "Wazzy"]) #TODO: Remove hardcoded sinners.
            embed = discord.Embed(
                    title="Sin Summary",
                    description=sin_summary_description,
                    color=discord.Color.brand_red()
            )
            if summary_message_id is None:
                await channel.send(embed=embed)
            else:
                message = await channel.fetch_message(summary_message_id)
                await message.edit(embed=embed)

        else:
            print(f"Could not access Channel ID: {channel_id}")

    except Exception as e:
        print(f"Could not post Sin Summary: {e}")

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
    if not SINS:
        await interaction.response.send_message("No sins found in the database.", ephemeral=True)
        return

    if cost:
        # Build a string listing all sins with their cost.
        # Use singular "Sin" if the count is 1, otherwise use plural "Sins".
        sins_list = "\n".join([
            f"**{sin[0]}** = {sin[2]} {'Sin' if sin[2] == 1 else 'Sins'}"
            for sin in SINS
        ])
    else:
        sins_list = "\n".join([f"**{sin[0]}** - {sin[1]}" for sin in SINS])

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
        app_commands.Choice(name="Coonah the Cuck", value=1),
        app_commands.Choice(name="Pat O'Well the Smell", value=2),
        app_commands.Choice(name="Rupert the Bear", value=3),
        app_commands.Choice(name="Wazzy the Wonderful", value=4)
    ], sin=SIN_NAMES)
async def add_sin_command(interaction: discord.Interaction, player: app_commands.Choice[int], sin: str):
    chosen_sin = next(s for s in SINS if s[0] == sin)
    sin_cost = chosen_sin[2] if len(chosen_sin) > 2 else 0
    success = add_sin_to_player(sin_cost, player.value)
    if success:
        await interaction.response.send_message(
            f"✅ **{player.name}** has been punished for **{sin}**! Sin recorded successfully.",
        )

bot.run(TOKEN)