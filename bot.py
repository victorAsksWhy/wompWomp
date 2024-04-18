import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members=True
intents.message_content=True


desc='''Ues /womp to post a womp womp gif. Good for trolling'''

bot = commands.Bot(command_prefix='/', description=desc, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}. ID: {bot.user.id}')
    print('**********')

@bot.command()
async def womp():
    await discord.TextChannel.send(file=discord.File('giphy.gif'))