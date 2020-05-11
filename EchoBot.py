print('Welcome to Echo Bot')

stuff_to_echo = input("What's your name?")

print("It's nice to meet you "+stuff_to_echo)

print("Welcome to Arturo's first chatbot!")
print("I will repeat after you.")
stuff_to_echo = input("Enter something for me to repeat: ")
print("You said: " + stuff_to_echo)
x = 1
while (x == 1):
	stuff_to_echo = input("Enter something for me to repeat: ")
	print("You said: " + stuff_to_echo)


# In creating Echo Chatbot, I implement
# some patterns that I’ll use as I develop more complex chatbot programs:
# 1. Greeting a user.
# 2. Informing the user that they are interacting with a bot (and not a human).
# 3. Instructing the user on how to interact with the bot.
# 4. Accepting user input.
# 5. Setting up output that is dependent on user input.
