import random

Action = ['My Hero Academia', 'Akame ga Kill', 'Bleach', 'Demon Slayer', 'Jujutsu Kaisen']
A = Action

Adventure = ['One Piece', 'Shield Hero', 'Overlord', 'Hunter x Hunter', 'Dr. Stone']
B = Adventure

def chooseAction():
    if prompt1=='action':
        random.choice(A)
def chooseAdven():
    if prompt1=='adventure':
        random.choice(B)

result1 = random.choice(A)
result2 = random.choice(B) 

prompt1=input('Which Anime Genre Would You Like? action or adventure?')

if prompt1=="action" or "adventure":
    prompt2=input("Would you like a list? or Should I choose for you?" "Type 'list' or 'choose'")
    if prompt2=="list":
            if prompt1=="action":
                print(A)
            elif prompt1=="adventure":
                print(B)
    elif prompt2=="choose":
            if prompt1=="action":
                chooseAction()
                print("You should watch" + " " + result1)
            elif prompt1=="adventure":
                chooseAdven()
                print("You should watch" + " " + result2)