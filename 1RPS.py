import random


ops=('Rock','Paper','Scissors')

run=True



while run:
    player=None
    computer=random.choice(ops)

    while player not in ops:


        player=input("Enter a choice:Rock,Paper,Scissor:-")

    print(f'Player:{player}')

    print(f'Computer:{computer}')


    if player == computer:

        print("It's a tie!")
    elif player =='Rock' and computer=="Scissors":
        print("You win!")
    elif player =="Paper" and computer=='Rock':
        print("You win!")
    elif player =='Scissors' and computer=="paper":
        print("You win!")
    else:
        print("You loose :(")

    if not input("Play Again? (Y/N):-").lower()=="y":
        run=False



print("Thanks for playing !!")
