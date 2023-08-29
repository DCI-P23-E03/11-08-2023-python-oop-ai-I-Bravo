import openai
import os 
from dotenv import load_dotenv 
from stringcolor import cs # For colored text
import tkinter as tk
from tkinter import scrolledtext
#from ai_assistant import ChatGPT
# api key again

load_dotenv()
APIKEY = os.getenv('APIKEY')
class ChatGPT:
    def __init__(self, api_key=APIKEY, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7, completions=1, presence_penalty=0.5, frequency_penalty=0.5):
        self.api_key = api_key
        self.model = model # The ChatGPT model used (gpt-3.5-turbo is an example, can be replaced)
        self.max_tokens = max_tokens # Maximum tokens allowed for response length
        self.temperature = temperature # 0.0 is deterministic, 1.0 is creative
        self.completions = completions # Number of completions per prompt
        self.presence_penalty = presence_penalty # The higher the value, the more likely new topics will be introduced
        self.frequency_penalty = frequency_penalty # The higher the value, the more likely information will be repeated
        openai.api_key = self.api_key

    def get_chatgpt_response(self, messages):
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

    def chat_interface(self):
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


class Waiter(ChatGPT):
     def __init__(self):
        super().__init__()  # Call the parent class constructor

        # Customize Waiter-specific attributes
        self.engine = "text-davinci-003"
        self.max_tokens = 100
        self.temperature = 0.8
        self.completions = 1
        self.best_of = 1
        self.presence_penalty = 0.2
        self.frequency_penalty = 0.0

#class DigitalWaiterChatbot:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("Digital Waiter Chatbot")

#        self.chat_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
#        self.chat_text.pack(padx=10, pady=10)

#        self.input_entry = tk.Entry(root, width=30)
#        self.input_entry.pack(padx=10, pady=10)

#        self.send_button = tk.Button(root, text="Send", command=self.send_message)
#        self.send_button.pack(padx=10, pady=10)

#        self.menu = {
#            "burger": 10,
#            "pizza": 12,
#            "pasta": 8,
#            "salad": 6
#        }

#        self.chat_text.insert(tk.END, "Digital Waiter: Welcome! How can I assist you?\n")
#        self.chat_text.config(state=tk.DISABLED)

#    def send_message(self):
#        user_input = self.input_entry.get().lower()
#        self.chat_text.config(state=tk.NORMAL)
#        self.chat_text.insert(tk.END, "You: " + user_input + "\n")

#        response = self.get_waiter_response(user_input)
#        self.chat_text.insert(tk.END, "Digital Waiter: " + response + "\n")
#        self.chat_text.config(state=tk.DISABLED)

#        self.input_entry.delete(0, tk.END)

#    def get_waiter_response(self, user_input):
#        if "menu" in user_input:
#            menu_items = ", ".join(self.menu.keys())
#            return f"Our menu includes: {menu_items}"
#        elif "order" in user_input:
#           return "What would you like to order?"
#        elif "bill" in user_input or "payment" in user_input:
#            return "Your bill is $XX. How would you like to pay?"
#        elif "thank you" in user_input:
#            return "You're welcome! Enjoy your meal!"
#        else:
#            return "I'm here to assist you with the menu, orders, and payments."

#def main():
#    root = tk.Tk()
#    app = DigitalWaiterChatbot(root)
#    root.mainloop()

#if __name__ == "__main__":
#    main()

if __name__ == '__main__':
    #api_key = APIKEY

    waiter_bot = Waiter()
    waiter_bot.chat_interface()
    



