#Rule Baased Ai Python ChatBoat 

import datetime
import time

name= input("Swagt h, enter your name:")
presentHour = datetime.datetime.now().hour

if 4<= presentHour <= 12:
    print("Good Morning!", name)
elif 11 <= presentHour <= 16:    
    print("Good Afternoon!", name)
elif 16 <= presentHour <= 21:
    print("Good Evening!", name)
else:
    print("Good Night!", name)

print("Namaste! Welcome to Your ChatBot.")
print("You can ask me basic question, Type 'bye' to exit from that bot.")

# Chatboat Memory Creation [dictionary of responses]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you?": "I am fine, thank you!",
    "who are you":  "I am samrt AI ChatBot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai": "jaker chapter 7 padho",
    "what about you": "I am just a bot, but I am learning new things every day!",
    "what is AI": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "bye": "Goodbye! Have a great day ahead."
}

# Method/Function to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. Mai jald hi ye sikh lunga"    


# Take user input

while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
       break



