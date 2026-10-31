def get_reply(user_input):
    """Return a predefined reply based on the user's message."""
    text = user_input.strip().lower()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm a simple Python chatbot."
    elif text == "help":
        return "Try: hello, how are you, what is your name, or bye."
    elif text in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' for ideas."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Chatbot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()