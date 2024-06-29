import random


responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm good, thank you!",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Exiting chatbot."
}


def respond(message):
    message = message.lower()  
    if message in responses:
        return responses[message]
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    response = respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() in ["bye", "exit"]:
        break
