# Basic Chatbot

def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user == "i am fine":
            print("Bot: That's great to hear!")
        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "thank you":
            print("Bot: You're welcome!")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
