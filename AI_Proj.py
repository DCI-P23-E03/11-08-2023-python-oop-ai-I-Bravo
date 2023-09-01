import openai
from stringcolor import *
import os
from dotenv import load_dotenv
import time 

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def display_welcome_message():
    print(cs("Welcome to LOREM IPSUM Restaurant!","orange"))
    print(cs("Describe what you're in the mood for, and I'll suggest a dish or drink.","darkgreen"))
    print(cs("Type 'quit' to exit the chat.\n","darkblue"))

class MenuItem:
    def __init__(self, name, properties, description):
        self.name = name
        self.properties = properties
        self.__description = description
    
    def get_description(self):
        return self.__description

class Dish(MenuItem):
    def __init__(self, name, properties, description):
        super().__init__(name, properties, description)

class Drink(MenuItem):
    def __init__(self, name, properties, description):
        super().__init__(name, properties, description)

# Sample Menu 
menu = [
    Dish("Steak", ["salty", "hot", "juicy", "savory"], "A sumptuous cut of Wagyu beef, grilled to perfection and seasoned with Himalayan salt and freshly ground black pepper."),
    Dish("Salad", ["fresh", "cold", "healthy", "light"], "A vibrant mélange of organic greens, handpicked heirloom tomatoes, and cruelty-free goat cheese, lightly dressed with a white truffle oil vinaigrette."),
    Drink("Iced Tea", ["cold", "sweet", "refreshing", "invigorating"], "An invigorating blend of hand-picked organic tea leaves, delicately brewed and chilled, sweetened with a hint of agave nectar."),
    Drink("Hot Coffee", ["hot", "bitter", "delicious", "bold"], "A meticulously crafted espresso blend from single-origin, shade-grown beans, extracted to perfection for a rich and bold experience."),
    Dish("Sushi", ["fresh", "cold", "savory", "umami"], "An exquisite selection of sushi featuring Bluefin tuna and Otoro, complemented by freshly grated wasabi and house-made soy sauce."),
    Dish("Pizza", ["hot", "cheesy", "salty", "crispy"], "A decadent artisanal pizza with a crispy sourdough crust, topped with buffalo mozzarella, San Marzano tomatoes, and a drizzle of 25-year-aged balsamic."),
    Dish("Pasta", ["warm", "creamy", "filling", "savory"], "House-made pappardelle pasta, tossed in a sumptuous truffle cream sauce and garnished with freshly shaved Parmigiano-Reggiano."),
    Drink("Smoothie", ["cold", "fruity", "creamy", "refreshing"], "A luxuriously smooth blend of rare tropical fruits, including açai and dragon fruit, mixed with organic coconut milk."),
    Drink("Lemonade", ["cold", "sweet", "tangy", "refreshing"], "A revitalizing concoction of freshly squeezed Amalfi lemons, balanced with a touch of organic cane sugar and mint."),
    Drink("Chai Tea", ["hot", "spiced", "sweet", "aromatic"], "A soothing elixir of single-origin Assam tea infused with a bespoke blend of spices, sweetened with pure Kashmiri saffron.")
]


def list_menu():
    print(cs("Certainly, allow me to present our selection of fine dishes and drinks.", "green"))
    for item in menu:
        print(f"{item.name}: {item.get_description()}")
        time.sleep(0.2)
# user
def get_user_input():
    return input("You: ")

def get_suggestion(user_input):
    matches = []
    for item in menu:
        if all(word in user_input for word in item.properties):
            matches.append(item)

    if matches:
        suggestion = matches[0]
        return f"How about trying the {suggestion.name}? {suggestion.get_description()}"
    else:
        return "I'm sorry, I couldn't find an exact match. Would you like to try something else?"

#openai
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
    system_role = "You are a waiter at LOREM IPSUM Restaurant, suggesting dishes/drinks based on customer mood. Your personality is like that of Rust Cohle from the series True Detective. You curse like Samuel L. Jackson." 
    messages = [{"role": "system", "content": system_role}] 
    
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'quit':
            break
        
        elif user_input.lower() == 'menu':
            list_menu()
            continue

        # Append user message to the message list
        messages.append({"role": "user", "content": user_input})
        
        # ok wtf
        if "menu" in user_input.lower():
            print(cs("Certainly, here is our exclusive menu:", "green"))
            for item in menu:
                print(cs(f"{item.name}: {item.get_description()}", "green"))

        # Check if user is looking for a suggestion
        elif any(word in user_input for word in ["salty", "hot", "cold", "sweet", "bitter", "fresh"]):
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
    