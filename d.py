import os
import discord
from dotenv import load_dotenv
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Imouto",
    database_uri="sqlite:///database.db"
)
client = discord.Client()
trainer = ListTrainer(bot) 

load_dotenv()

@client.event
async def on_ready():
    print('We have logged in')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("train"):
        await message.channel.send("train me oni chan")
    if message.content.startswith("test"):
        await message.channel.send("Owo testing")


client.run(os.getenv("BOT_TOKEN"))

