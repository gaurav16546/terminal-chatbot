# bot.py
from chatterbot import ChatBot,filters
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus

# CORPUS_FILE = "chat.txt"

chattbot = ChatBot(
    "Chatpot",
    filters=[filters.get_recent_repeated_responses],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
                    "chatterbot.logic.UnitConversion",
    ]
)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.science",
    "chatterbot.corpus.english.computers",
    "./chatterbot_corpus/data/computer_science.yml")

# trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)
while True:
    try:
        user_input = input()

        bot_response = chattbot.get_response(user_input)

        print(f"🤖 {bot_response}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break