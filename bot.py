from re import search
import aiohttp
import discord
from discord import channel
from discord import message
from discord.flags import Intents
from dotenv import load_dotenv
import os
import random

api_chuck = "https://api.chucknorris.io/jokes/random"
api_search_chuck = "https://api.chucknorris.io/jokes/search?query="

load_dotenv()
TOKEN = os.getenv("TOKEN_DS")
GUILD = int(os.getenv("GUILD_DS"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("€random"):
        async with aiohttp.ClientSession() as session:
            async with session.get(api_chuck) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send(js["value"])

    if message.content.startswith("€search "):
        search_term = message.content[8:]
        busqueda = api_search_chuck+search_term
        async with aiohttp.ClientSession() as session:
            async with session.get(busqueda) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send(random.choices(js["result"])[0]["value"])
                    

client.run(TOKEN)