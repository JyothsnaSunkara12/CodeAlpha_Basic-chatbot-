"""
Basic Rule-Based Chatbot
Description: A simple chatbot using predefined rules.
Concepts Used: if-elif, functions, loops, input/output
"""

def greet():
    return "Hi!"

def how_are_you():
    return "I'm fine, thanks!"

def goodbye():
    return "Goodbye!"

def fallback():
    return "Sorry, I didn't understand that."

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

        # Greetings
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    # Personal questions
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! What about you?"

    elif user_input in ["what is your name", "your name", "who are you"]:
        return "My name is BasicBot."

    elif user_input in ["what are you doing", "what are you up to"]:
        return "I'm chatting with you."

    elif user_input in ["what about you", "tell me about yourself"]:
        return "I am a simple Python rule-based chatbot."

    # Time and date
    elif user_input == "what is the time":
        return "Sorry, I cannot check real time yet."

    elif user_input == "what is today's date":
        return "Sorry, I cannot check today's date yet."

        # Thank you
    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"

    # Goodbye
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a nice day."

    else:
        return fallback()


def run_chatbot():
    print("Basic Chatbot (type 'bye' to exit)\n(Use formal text.)\n")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break


# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
