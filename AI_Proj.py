import openai
from stringcolor import *
import os
from dotenv import load_dotenv
#import time '''<<<<maybe for later use of sleep functions for paused text execution'''

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def display_welcome_message():
    print(cs("Welcome to WASSUP Restaurant!","blue"))
    print(cs("Describe what you're in the mood for, and I'll suggest a dish or drink.","darkblue"))
    print(cs("Type 'quit' to exit the chat.\n","darkblue"))

class MenuItem:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties
        self.__description = description
    
    #def get_description(self):
        #return self.__description

class Dish(MenuItem):
    def __init__(self, name, properties):
        super().__init__(name, properties)

class Drink(MenuItem):
    def __init__(self, name, properties):
        super().__init__(name, properties)

# Sample Menu needs more shit
menu = [
    Dish("Steak", ["salty", "hot"]),
    Dish("Salad", ["fresh", "cold", "gay"]),
    Drink("Iced Tea", ["cold", "sweet", "refreshing"]),
    Drink("Hot Coffee", ["hot", "bitter", "delicious"]),
]

# user
def get_user_input():
    return input("You: ")

def get_suggestion(user_input):
    matches = []
    for item in menu:
        if all(word in user_input for word in item.properties):
            matches.append(item.name)

    if matches:
        return f"How about trying the {matches[0]}?"
    else:
        return "I'm sorry, I couldn't find an exact match. Would you like to try something else?"

#openai aaaallll the way dooowwwnn
def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # gpt model name
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        n=1,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    return response.choices[0].message['content']

# The chat interface loop
def chat_interface():
    display_welcome_message()
    system_role = "You are a waiter at WASSUP Restaurant, suggesting dishes/drinks based on customer mood. You curse like Samuel L. Jackson"
    messages = [{"role": "system", "content": system_role}] 
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'quit':
            break

        # Append user message to the message list
        messages.append({"role": "user", "content": user_input})

        # Check if user is looking for a suggestion
        if any(word in user_input for word in ["salty", "hot", "cold", "sweet", "bitter", "fresh"]):
            suggestion = get_suggestion(user_input)
            print(cs(suggestion,"green"))
        else:
            # Get AI response and append to messages
            ai_response = get_chatgpt_response(messages)
            print(cs(ai_response,"green"))
            messages.append({"role": "assistant", "content": ai_response})

# Run the chat interface
if __name__ == '__main__':
    chat_interface()


# count gpt tokens
'''
import tiktoken

def count_tokens(text):
    enc = tiktoken.encoding_for_model("text-davinci-003")
    tokens = len(enc.encode(text))
    tokens_left = 4096 - tokens
    return tokens
'''

