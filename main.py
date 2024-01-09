# Welcome message

print("Welcome to the Elite 101 Chatbot!")

# User information collection

name = input("Please enter your name: ")

age = int(input(f"Nice to meet you, {name}! How old are you? "))

if age < 15:
  print(f"Welcome {name}! Oh it would be great to be back in my youth! How can I help you today?")
elif age < 18:
  print(f"Welcome {name}! Hey you got your whole life ahead of you! How can I help you today?")
elif age < 55:
  print(f"Welcome {name}! Ah! The thrills of adulthood! How can I help you today?")
elif age < 120:
  print(f"Welcome {name}! Wow! Quite the span of experiences! How can I help you today?")
elif age > 120:
  print(f"Welcome {name}! Wow! Breaking records with that age! How can I help you today?")
else:
  print("Sorry, try again.")

# Conversation menu function

def convoMenu():
  print("Please choose from the following options:")
  print("1. Placeholder Option 1")
  print("2. Placeholder Option 2")
  print("3. Placeholder Option 3")
  print("4. Exit the conversation")

# Conversation menu

convoMenu()
convo = int(input("Enter the number of your choice: "))

if convo == 1:
  print("This is a Placeholder for now :)")
elif convo == 2:
  print("This is a Placeholder for now :)")
elif convo == 3:
  print("This is a Placeholder for now :)")
elif convo == 4:
  print(f"Goodbye, {name}! Have a great day!")
else:
  print("Please choose one of the four options.")