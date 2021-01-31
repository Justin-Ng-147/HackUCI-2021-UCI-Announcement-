import discord
import os
from ics import Calendar, Event

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}.format'(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!events'):
    await message.channel.send('Command test successful')

client.run(os.getenv('TOKEN'))
