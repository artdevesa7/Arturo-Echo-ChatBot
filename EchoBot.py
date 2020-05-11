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


# In creating Echo Chatbot, you’re already implementing 
# some patterns that you’ll use as you develop more complex chatbot programs:
# Greeting a user.
# Informing the user that they are interacting with a bot (and not a human).
# Instructing the user on how to interact with the bot.
# Accepting user input.
# Setting up output that is dependent on user input.
# Want to extend this project further? Try adding more lines of input and output to craft a 
# funny sort of conversation. 
# You can also ask for the user’s name and then use it in subsequent outputs.