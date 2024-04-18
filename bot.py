import discord
from discord.ext import commands

import discord.ext
import discord.ext.commands


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('---------------')


@bot.command()
async def womp(ctx):
    await ctx.send(file=discord.File('giphy.gif'))

bot.run('MTIzMDE1MTk2Njk3MDM0NzY0MQ.Gp97DL.wPtZf6xxcpIgmg4_jEaCcCfZ0WZ4tDnJUqrtH8')