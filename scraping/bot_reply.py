




from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot("InfoConnect Bot")
# conv1=['What is your name?', 'My name is Cool Guy']
# conv2=['Who are you?', 'I am a bot, created by Archit' ]
#
# trainer=ListTrainer(bot)
# trainer.train(conv1)
# trainer.train(conv2)
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")

#
# a=input()
# while a!="Bye":
#     resp=bot.get_response(a)
#     print(resp)
#     a=input()
