from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Hajime's sister",
  database_uri="sqlite:///database.db"
)

trainer = ListTrainer(bot)
'''
trainer.train([
  "sex",
  "no"
])
'''

print(bot.get_response("sex"))

