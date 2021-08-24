import random

def guessthenumber(x):
    randomnumber=random.randint(1,x)
    guess=0
    while guess != randomnumber:
        guess=int(input(f"Guess a no. between 1 and {x}:"))
        if guess <randomnumber:
            print("Oops!! Too Low")
        elif guess>randomnumber:
            print("Oops!! Too High")
    print (f"Yasss!! You have guessed the number {randomnumber} correctly!!")
x=int(input("number:"))
guessthenumber(x)