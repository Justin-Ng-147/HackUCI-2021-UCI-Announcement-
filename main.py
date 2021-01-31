import discord
import os
from getdata import get
from dotenv import load_dotenv
import redis

load_dotenv('a.env')
Token = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!events'):
    #msg = message.content[7:]
    #print(get(msg))
    #for send in get(msg):
    #    await message.channel.send(send)
    channel = discord.utils.get(client.get_all_channels(), name='calendar')
    channel_id = channel.id

    msgs = await client.get_channel(channel_id).history(limit=5).flatten()
    last5 = []
    for msg in msgs:
        last5.append(msg.content)

    for cal in last5:
        try:
            embedVar = discord.Embed(title="Todays Events",color = 0xCABD97)
            if get(cal) != None and get(cal) != []:
                for event in get(cal):
                    event_list = event.splitlines()
                    embedVar.add_field(name=event_list[0], value='\n'.join(event_list[1:]), inline=False)
            else:
                embedVar.add_field(name='No Events For Today',value='')
            await message.channel.send(embed=embedVar)
        except AssertionError:
            embedVar = discord.Embed(title=f"Error, {cal} does not lead to valid ics file",color = 0xCABD97)
            await message.channel.send(embed=embedVar)

#redis_server = redis.Redis()

client.run(Token)