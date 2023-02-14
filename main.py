# This example requires the 'message_content' privileged intents

import os
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    sayings = ['I love pancakes!', 'Go Warriors!',
               'Spark! is the best place to work on campus.', 'West coast best coast.', 'The Mandalorian is the best Disney+']

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


    if message.content.startswith('$josh'):
        saying = random.sample(sayings, 1)[0]
        name = message.author.name
        await message.channel.send("Hi " + name + "! " + saying)



client.run(os.environ["DISCORD_TOKEN"])
