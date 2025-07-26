import re
from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Rule 1: Greeting
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Chatbot: Hello there! How can I assist you?")

        # Rule 2: Asking about chatbot's name
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your friendly assistant!")

        # Rule 3: Asking about time
        elif "time" in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")

        # Rule 4: Thank you
        elif re.search(r"\b(thank you|thanks)\b", user_input):
            print("Chatbot: You're welcome!")

        # Rule 5: Asking for help
        elif "help" in user_input:
            print("Chatbot: I can help you with basic questions like greetings, time, and simple info.")

        # Default fallback
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you try rephrasing it?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
