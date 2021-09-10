# We'll use it to tokenize strings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# regex library
import re
# sqlite database
import sqlite3 as sqlite
# discord for easily training
from discord.ext import commands
# dotenv in python
from dotenv import load_dotenv
# os for reading env variables
import os

prefix = "_"
load_dotenv()

client = commands.Bot(command_prefix="_")
conn = sqlite.connect("data.db")

cursor = conn.cursor()

# The input array
f_a = []
# The output array
f_b = []
# The expression array
f_e = []
# Add from db to arrays
sq_rows = cursor.execute("SELECT * FROM data")
for d in sq_rows.fetchall():
    f_a.append(d[0])
    f_b.append(d[1])
    f_e.append(d[2])


def remove_punctuation(text):
    return re.sub(r'[^\w\s]', "", text)

def lemmatize(text):
    # The result array
    # We'll return it at the end
    result = []
    # The lemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    # Tokenize ueach word as a sententse
    bb = nltk.word_tokenize(remove_punctuation(text))
    # Run a loop throw the word array
    for c in bb:
        # Lemmatize each word (turned into lower)
        l = lemmatizer.lemmatize(c.lower())
        result.append(l)
    return result

def get(text):
    # The tutorial I followed did this
    # So I'm doing this
    f_a.append(text)
    # Turn tokens into vectors
    tfidf = TfidfVectorizer(tokenizer = lemmatize).fit_transform(f_a)
    # Get similarity of all strings
    similarity = cosine_similarity(tfidf[-1], tfidf).flatten()
    # The one with highest match is the given string itself
    # So we choose the second one
    best = similarity.argsort()[-2]
    # if The best one has zero match
    if similarity[best] == 0:
        # No result
        return("I couldn't get that oni chan")
    else:
        #so we don't fuck things up
        f_a.remove(text)
        # put return instead of print in production
        return(f_b[best])
        # return f_e[best] in app version
def set(a,b):
    try:
        # add emotion later
        cursor.execute("INSERT INTO data(a,b) VALUES(?,?)", (a, b))
        conn.commit()
        f_a.append(a)
        f_b.append(b)
        #f_e.append(e)
    except:
        print("Something went wrong")
#set("Morning", "Ohio, oni-chan!")
print(get("Morning nee-san"))


@client.command(name = "train")
async def train(ctx, *args):
    if len(args) < 1:
        return await ctx.reply("Go awoo")
    else:
        text = str(ctx.message.content)[len(prefix + "train "): len(ctx.message.content)]
        ar = text.split("\n")
        if (len(ar) <2) or (len(ar) >3):
            return await ctx.reply("Noooooo")
        else:
            a = ar[0]
            b = ar[1]
            #e = ar[3].lower()
            set(a, b)
            return await ctx.reply("added `"+ b + "` for `" + a + "`")
@client command(name = "test")
async def test(ctx, *args):
    if len(args) < 1:
        return await ctx.reply("Shooo")
    else:
        text = " ".join(args)
        return await ctx.reply(get(text))
client.run(os.getenv("BOT_TOKEN"))
