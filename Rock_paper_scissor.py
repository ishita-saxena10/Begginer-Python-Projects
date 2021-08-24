import random
#r>s , p>r , s>p
def rockpaperscissor():
    user=input("what's your choice?'r' for rock,'p' for paper,'s' for scissor")
    computer=random.choice(['r','p','s'])
    print ("Computer's choice",computer)

    if user==computer:
        print ("Tie")
    
    if win(user, computer):
        return 'You won!'

    return 'You lost!'
    
def win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print (rockpaperscissor())