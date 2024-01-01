# bot.py
from chatterbot import ChatBot,filters
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus

# CORPUS_FILE = "chat.txt"

chatbot = ChatBot(
    "Chatpot",
    filters=[filters.get_recent_repeated_responses],
    logic_adapters=[
        "chatterbot.logic.BestMatch",
         'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ]
    )
trainer = ChatterBotCorpusTrainer("chatterbot.corpus.english")
# trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)
exit_conditions = (":q","quit","exit")
while True:
    query = input("< ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")