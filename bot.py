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
    print(f'Logged in as {bot.user} with ID: {bot.user.id}')
    print('---------------')


@bot.command()
async def womp(ctx):
    '''Post a womp womp womp gif'''
    await ctx.send(file=discord.File('giphy.gif'))

@bot.command()
async def spam(ctx, message, times):
    '''Spam a message'''
    times = int(times)
    for x in range(times):
        await ctx.send(message)


bot.run('MTIzMDE1MTk2Njk3MDM0NzY0MQ.Gp97DL.wPtZf6xxcpIgmg4_jEaCcCfZ0WZ4tDnJUqrtH8')