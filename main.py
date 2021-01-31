import discord
import os
from getdata import get

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!events'):
    msg = message.content[7:]
    print(get(msg))

    await message.channel.send(get(msg)[0])

client.run('ODA0OTE3NTA5MjQ4OTA5MzIz.YBTT2A.-OtAWlAdyJSXQeA14eW-2TUfYek')

    await message.channel.send(get(msg))

client.run(os.getenv('TOKEN'))

