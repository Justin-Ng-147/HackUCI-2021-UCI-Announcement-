import discord
import redis
import os
from getdata import get

redis_server = redis.Redis()
client = discord.Client()
AUTH_TOKEN = str(redis_server.get(‘AUTH_KEY’).decode(‘utf-8’))
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

client.run(AUTH_TOKEN)
  
