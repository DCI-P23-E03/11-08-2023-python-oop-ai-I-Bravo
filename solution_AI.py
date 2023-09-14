import openai
import os 
from dotenv import load_dotenv # library used for managing environment variables through a .env file
from stringcolor import cs # For colored text
import tkinter as tk # creating graphical user interface
from tkinter import scrolledtext  # is handy for getting text from a text widget such as creating text editors, log viewers etc.
#from ai_assistant import ChatGPT
# api key again

load_dotenv()
APIKEY = os.getenv('APIKEY')
class ChatGPT:  # class serves as the core chatbot class WHICH IS THE PARENT CLASS
    def __init__(self, api_key=APIKEY, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7, completions=1, presence_penalty=0.5, frequency_penalty=0.5):
        self.api_key = api_key
        self.model = model # The ChatGPT model used (gpt-3.5-turbo is an example, can be replaced)
        self.max_tokens = max_tokens # Maximum tokens allowed for response length
        self.temperature = temperature # 0.0 is deterministic, 1.0 is creative
        self.completions = completions # Number of completions per prompt
        self.presence_penalty = presence_penalty # The higher the value, the more likely new topics will be introduced
        self.frequency_penalty = frequency_penalty # The higher the value, the more likely information will be repeated
        openai.api_key = self.api_key
# SUB CLASS OF CHATGPT: IT HANDLES THE AI'S ROLE
    def get_chatgpt_response(self, messages): # function that takes in a list of messages and returns a list of responses
        response = openai.ChatCompletion.create(
            model=self.model, # ChatGPT model
            messages=messages, # Ongoing conversation
            temperature=self.temperature, # Chosen temperature (creativity/strictness)
            max_tokens=self.max_tokens, # Maximum tokens allowed
            n=self.completions, # Number of completions
            presence_penalty=self.presence_penalty, # Chosen new-topics-probability
            frequency_penalty=self.frequency_penalty # Chosen repeat-info-probability
        )
        choices = [choice.message['content'] for choice in response.choices] # Extracting the content of responses
        return choices
# SUB CLASS OF CHATGPT: IT HANDLES THE USER'S ROLE
    def chat_interface(self): # handles the conversation between the user and the AI. It continually asks for user input and displays the AI's response. In this case simulating a waiter.
        # Display welcome message
        print(cs("Welcome to ChatGPT!", "blue"))
        print(cs("Type 'quit' to exit the chat.\n", "darkblue"))
        system_role = "You are a digital waiter" # DEFINE SYSTEM ROLE HERE
        messages = [{"role": "system", "content": system_role}] 
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            messages.append({"role": "user", "content": user_input}) # Append user's input to messages
            responses = self.get_chatgpt_response(messages) # Get responses from ChatGPT
            print("CHAT GPT: ")
            for resp in responses:
                print(cs(resp, "green")) # Display AI's response in green
                messages.append({"role": "assistant", "content": resp}) # Append AI's response to messages

# IT INHERITS FROM THE CHATGPT CLASS
class Waiter(ChatGPT):   #sub class of ChatGPT: it handles the waiter's role
     def __init__(self): # method that calls for the constructor of the superclass using the super() function
        super().__init__()  # Call the parent class constructor

        # Customize Waiter-specific attributes
        self.engine = "text-davinci-003"
        self.max_tokens = 100
        self.temperature = 0.8
        self.completions = 1
        self.best_of = 1
        self.presence_penalty = 0.2
        self.frequency_penalty = 0.0

if __name__ == '__main__':  # instance of of the Waiter class
    #api_key = APIKEY

    waiter_bot = Waiter()
    waiter_bot.chat_interface() # Start chat interface








