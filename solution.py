from dotenv import load_dotenv
import os
import openai # importing the almighty openai library
from stringcolor import *

load_dotenv()

# api key again
key = os.getenv('API_KEY')

class ChatGPT:
    def __init__(self, api_key=key, model_engine="gpt-4", max_tokens=150, temperature=0.7, completions=1, presence_penalty=0.5, frequency_penalty=0.5):
        self.api_key = api_key
        self.engine = model_engine # engine is the chatgpt model used, davinci is the smartest, fastest yet most expensive
        self.max_tokens = max_tokens # maximum tokens allowed for response length
        self.temperature = temperature #  0.0 is deterministic, completely strict to system role - 1.0 is creative, completely random responses (now choose)
        self.completions = completions # number of completions per prompt
        self.presence_penalty = presence_penalty # the higher the value, the more likely new topics will be introduced
        self.frequency_penalty = frequency_penalty # the higher the value, the more likely information will be repeated
        openai.api_key = self.api_key

    def get_chatgpt_response(self, messages):
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=messages,
            max_tokens=self.max_tokens,
            n=self.completions,
            temperature=self.temperature,
            presence_penalty =self.presence_penalty,
            frequency_penalty=self.frequency_penalty
        )
        choices = [choice.message['content'] for choice in response.choices] # Extracting the content of responses
        return choices
        
    def chat_interface(self):
        # Display welcome message
        print(cs("Welcome to the Digital Waiter Chatbot!", "blue"))
        print(cs("Type 'quit' to end the conversation.\n", "darkblue"))
        system_role = "You are a Waiter in a restuarant" # DEFINE SYSTEM ROLE HERE
        messages = [{"role": "system", "content": system_role}] 
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            messages.append({"role": "user", "content": user_input}) # Append user's input to messages
            responses = self.get_chatgpt_response(messages) # Get responses from ChatGPT
            print("Waiter: ")
            for resp in responses:
                print(cs(resp, "green")) # Display AI's response in green
                messages.append({"role": "assistant", "content": resp})



if __name__ == '__main__':
    
    waiter_bot = ChatGPT()
    waiter_bot.chat_interface()
    

