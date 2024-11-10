import random

greet = ["hello", "hey", "hi", "ohho"]
intro = "I am your friend mr.chat, chat with me!!!"
query = {
    "product": ["Which product do you need?"],
    "service": ["Which service do you need?"],
    "contact": ["Which contact do you need?"],
    "policies": ["Which policies do you need?"],
    "default": ["Sorry, I don't get the point."]
}
task = ["Sure, I will do that."]
goodbye = ["Goodbye! We will meet again. Love you, dear!!"]  # Changed from 'bey'

def greetme():
    print(random.choice(greet))
    print(intro)

def queryfier(user_input):  # Renamed the parameter to avoid confusion
    if "product" in user_input:
        print(random.choice(query["product"]))
    elif "service" in user_input:
        print(random.choice(query["service"]))
    elif "contact" in user_input:  # Corrected spelling of 'contact'
        print(random.choice(query["contact"]))
    elif "policies" in user_input:
        print(random.choice(query["policies"]))
    else:
        print(random.choice(query["default"]))

def assist():
    print(random.choice(task))

def goodbey():  # Corrected spelling of 'goodbye'
    print(random.choice(goodbye))

def main():
    greetme()
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            break
        queryfier(user_input)
        assist()
    goodbey()

if __name__ == "__main__":
    main()
