def chatbot():
    print("========== BASIC CHATBOT ==========")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thank you!")

        elif user == "what is your name":
            print("Bot: My name is Python ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "help":
            print("Bot: You can say hello, how are you, or bye.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()