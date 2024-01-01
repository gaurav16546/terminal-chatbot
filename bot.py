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
        {
            "import_path":"chatterbot.logic.BestMatch",
            # 'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
            # "response_selection_method": chatterbot.response_selection.get_first_response
        }
    ]
)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.science",
    "chatterbot.corpus.english.computers",
    "chatterbot.corpus.english.emotion",
    "chatterbot.corpus.english.humor")

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