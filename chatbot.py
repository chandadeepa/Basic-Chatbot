print("=== Basic Chatbot ===")

while True:

    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")