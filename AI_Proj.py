import openai
from stringcolor import *
import os
from dotenv import load_dotenv

load_dotenv()



# Make sure to set up your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Display welcome message to the user
def display_welcome_message():
    print(cs("Welcome to ChatGPT!","blue"))
    print(cs("Type 'quit' to exit the chat.\n","darkblue"))

# Get user input
def get_user_input():
    return input("You: ")

# Use AI to generate a response
def get_chatgpt_response(messages, completions:int):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Using gpt-3.5-turbo as an example; replace with gpt-4 if u want to
        messages=messages,      # The ongoing conversation
        temperature=0.7,
        max_tokens=150,
        n=completions,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    choices = [choice.message['content'] for choice in response.choices]
    return choices

# The chat interface loop
def chat_interface():
    display_welcome_message()
    system_role = "You are Rust Cohle from the TV Series True Detective. You speak and behave like him but you curse like Samuel L. Jackson" # DEFINE SYSTEM ROLE HERE
    messages = [{"role": "system", "content": system_role}] 
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'quit':
            break

        # Append user message to the messages list
        messages.append({"role": "user", "content": user_input})

        #Get AI response and append to messages
        responses = get_chatgpt_response(messages, 1)           # choose how many completions you want
        print("CHAT GPT: ")
        for resp in responses:
            print(cs(resp,"green"))
            messages.append({"role": "assistant", "content": resp})
        #print(messages) #if you want system messages, uncomment that shit

# Run the chat interface
if __name__ == '__main__':
    chat_interface()
