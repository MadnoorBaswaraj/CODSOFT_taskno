print("welcome to ROCK PAPER SCISSORS game")
import random
options=['rock','paper','scissors']
#print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\n")
while True:
    user_choice=input("enter ur choice rock paper scissors")
    comp_choice=random.choice(options)
    #print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\n")
    if user_choice==comp_choice:
        print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\n MATCH IS TIE\n")
    elif user_choice=="paper":
        if comp_choice=="rock":
            print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\nYou Win The Match")
        else:
            print("fYour choice\n{user_choice}\ncomp choice\n{comp_choice}\nYOU LOOSE THE MATCH")
    elif user_choice=="scissors":
        if comp_choice=="paper":
            print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\nYou Win The Match")
        else:
            print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\nYOU LOOSE THE MATCH")
    elif user_choice=="rock":
        if comp_choice=="scissors":
            print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\nYou Win The Match")
        else:
            print(f"Your choice\n{user_choice}\ncomp choice\n{comp_choice}\nYOU LOOSE THE MATCH")
    else:
        print("enter valid option")
            
        