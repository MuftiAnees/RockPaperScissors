from random import random
import random

computerChoice= random.choice(['r','p','s'])
print("Welcome to Rock Paper and Scissors Game\nPress 'r' for Rock, 'p' for Paper, and 's' for Scissors.")
choice=input("Enter Your Choice.")

if choice==computerChoice:
    print("It is a tie")

elif (choice=='r' and computerChoice=='s') or (choice=='p' and computerChoice=='r') or (choice=='s' and computerChoice=='p'):
    print("You Win")
else:
    print("You Lost!")