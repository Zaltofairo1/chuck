import aiohttp
import discord
from discord import channel
from discord import message
from discord.flags import Intents
from dotenv import load_dotenv
import os

api_chuck = "https://api.chucknorris.io/jokes/random"

load_dotenv()
TOKEN = os.getenv("TOKEN_DS")
GUILD = int(os.getenv("GUILD_DS"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
print(os.getenv("USERNAME"))

@client.event
async def on_ready():
    print ("Ready!!!")

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

client.run(TOKEN)