import nltk
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Download the NLTK punkt tokenizer
nltk.download('punkt')

from nltk.chat.util import Chat, reflections

# Define some basic patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to assist you with basic queries.",]
    ],
    [
        r"how are you ?",
        ["I am doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon :)"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to process user input using spaCy
def process_input(user_input):
    doc = nlp(user_input)
    return doc

# Function to chat with the user
def chat():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Take care. See you soon :)")
            break
        processed_input = process_input(user_input)
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
