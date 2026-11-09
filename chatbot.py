print("Hello I am a chatbot. What is your name?")

name = input()

print(f"Nice to meet you,{name}!")

print("How are you feeling today?(good/bad)")
mood= input().lower()

if mood=="good":
    print("I'm glad to hear that!")

elif mood=="bad":
    print("I'm sorry to hear that I hope it gets better soon")

else:
    print("I see, sometimes its hard to put feelings into words")

print(f"It was nice chatting with you {name}. bye")
