#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import discord
from keep_alive import keep_alive
my_secret = os.environ['token']


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Amenofis') or message.content.startswith('amenofis'):
        await message.channel.send('Dispensi?')

    if message.content.startswith('Jordi') or message.content.startswith('jordi'):
        await message.channel.send('Jetpack')

    if message.content.startswith('Jetpack') or message.content.startswith('jetpack'):
        await message.channel.send('Jordi')

    if message.content.startswith('Wolframi') or message.content.startswith('wolframi'):
        await message.channel.send('Tungstè')

    if message.content.startswith('tungstè')or message.content.startswith('Tungstè') or message.content.startswith('tungste') or message.content.startswith ('Tungste'):
        await message.channel.send('Wolframi')
    
    if message.content.startswith('Gos') or message.content.startswith('gos'):
        await message.channel.send('Gat')
    
    if message.content.startswith('Gat') or message.content.startswith('gat'):
        await message.channel.send('Ocell')

    if message.content.startswith('Llom') or message.content.startswith('llom'):
        await message.channel.send('Diplodocus')

keep_alive()
client.run(my_secret)

