from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot("CustomerBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train("chatterbot.corpus.english")

# Define a function to interact with the chatbot
def customer_interaction():
    print("Customer: Hello!")
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("CustomerBot:", response)

# Start customer interaction
customer_interaction()
