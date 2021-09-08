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

def train(a, b):
    return trainer.train([ a, b ])
def test(a):
    return bot.get_response(a)

@client.event
async def on_ready():
    print('We have logged in')


@client.event
async def on_message(message):
    if message.author == client.user:
        return(False)
    if message.content.startswith("train"):
        a = message.content[len("train "): len(message.content)].split("\n")
        if len(a) != 2:
            return await message.channel.send("UwU wrong format")
        train(a[0], a[1])
        return message.channel.send("You trained me so hard onii chan")
    if message.content.startswith("test"):
         a = message.content[len("test"): len(message.content)]
        if len(strip(a)) <= 0:
            return message.channel.send("Baka !!\nWrong format")
        return message.channel.send(test(strip(a)))


client.run(os.getenv("BOT_TOKEN"))

