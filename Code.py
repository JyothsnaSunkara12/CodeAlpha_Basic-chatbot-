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

    if user_input == "hello":
        return greet()

    elif user_input == "how are you":
        return how_are_you()

    elif user_input == "bye":
        return goodbye()

    else:
        return fallback()


def run_chatbot():
    print("Basic Chatbot (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break


# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
