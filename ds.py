from discord.ext import commands
from dotenv import load_dotenv
import os

prefix = "_"
load_dotenv()
client = commands.Bot(command_prefix="_")

@client.command(name = "train")
async def train(ctx, *args):
    if len(args) < 1:
        return await ctx.reply("Go awoo")
    else:
        text = str(ctx.message.content)[len(prefix + "train "): len(ctx.message.content)]
        ar = text.split("\n")
        print(text)
        print(ar)
        if (len(ar) <2) or (len(ar) >3):
            return await ctx.reply("Noooooo")
        else:
            a = ar[0]
            b = ar[1]
            #e = ar[3].lower()
            await ctx.reply('"'+ a + '", "'+ b + '"')

client.run(os.getenv("BOT_TOKEN"))
