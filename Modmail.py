
import discord
from discord.ext import commands

intents = discord.Intent.default()

intents.members = True

bot = commands.bot(command_prefix = "=", intents = intents)

@bot.event
async def on_ready():
    print("KLM Modmail bot is ready!")
    bot.load_extension("cogs.onMessage")

bot.run("")