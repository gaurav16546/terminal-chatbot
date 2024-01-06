# bot.py
from chatterbot import ChatBot,filters
import logging
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from cleaner import clean_corpus
from give_feedback import feedback_loop
from bot_program import bot_program

# CORPUS_FILE = "chat.txt"
logging.basicConfig(level=logging.INFO)
chattbot = ChatBot(
    "Chatpot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
         {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Bring me your father.',
            'output_text': 'Ok, here is a link: https://chat.openai.com/'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            # 'maximum_similarity_threshold': 0.90
        },
                    "chatterbot.logic.UnitConversion",
                    'chatterbot.logic.MathematicalEvaluation',
    ]
)

trainer = ListTrainer(chattbot)
corpus_trainer = ChatterBotCorpusTrainer(chattbot)
corpus_trainer.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.science",
    "chatterbot.corpus.english.computers",
    "./chatterbot_corpus/data/computer_science.yml")

# trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)

print("Enter whether you want to run simple program or want to run feedback program?")
print("1 for simple program\n2 for feedback program")
choice = input()
if(choice == '1'):
    bot_program(chattbot)
elif(choice == '2'):
    feedback_loop(chattbot,trainer)
else:
    print("Invalid input")