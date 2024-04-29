import random
import os
def clear():
    os.system("clear")
clear()
age = int(input("Enter the year you were born: ").strip())
isYoung = None
if age < 2008:
    isYoung = False
else:
    isYoung = True
input("Press enter to continue: ")
clear()
isGoodAtGames = None
options = ["rock", "paper", "scissors"]
print("Ok...Now let's play a game of rock-paper-scissors!")
userChoice = input("Enter your choice: 'rock,' 'paper,' or 'scissors': ").lower().strip()
computerChoice = random.choice(options)
while computerChoice == userChoice:
    computerChoice = random.choice(options)

if (computerChoice == "rock" and userChoice == "scissors") or \
   (computerChoice == "paper" and userChoice == "rock") or \
   (computerChoice == "scissors" and userChoice == "paper"):
    print(f"The computer chose {computerChoice} and won!")
    isGoodAtGames = False
elif (computerChoice == "rock" and userChoice == "paper") or \
     (computerChoice == "paper" and userChoice == "scissors") or \
     (computerChoice == "scissors" and userChoice == "rock"):
    print(f"The computer chose {computerChoice}, you chose {userChoice}, so you beat the computer!")
    isGoodAtGames = True
else:
    print("You're bad at typing and had a typo in your choice...moving on...")
def checkVal(val):
    return False if val > 21 else True
isLucky = None
input("Press enter to continue: ")
clear()
print("Now you're going to play a twisted game of blackjack.")
startingVal = random.randint(3, 13)
print(f"Your starting value is {startingVal}")
choice = int(input("Enter '1' to get a new random card or '2' to stop where you are and keep your cards: "))
if choice == 1:
    newCard = random.randint(3, 13)
    print(f"Your new card is {newCard}. Added to your existing value of {startingVal}, your new total is {newCard + startingVal}.")
    if checkVal(newCard + startingVal):
        print("Dang, you're lucky and ended up with less than 21. Moving on to the next game...")
        isLucky = True
    else:
        print("I guess you're not so lucky, your value exceeded 21! Moving on to the next game...")
        isLucky = False
elif choice == 2:
    print("You're lame. I guess you don't want to push your luck, but still, lame. Moving on...")
    isLucky = False
else:
    print("You're bad at typing. I said enter '1' or '2'. Moving on...")
    isLucky = False
input("Press enter to continue: ")
clear()
num1 = random.randint(2, 12)
num2 = random.randint(2, 12)
ans = num1 * num2
userAns = int(input(f"Answer this math question:\n{num1} X {num2}\n> ").strip())
isSmort = None
if userAns == ans:
    print("You're smort. You got it right.")
    isSmort = True
else:
    print(f"How did you get it wrong?! The answer was {ans}. Not smort.")
    isSmort = False
input("Enter to continue: ")
clear()
if isSmort or isLucky or isGoodAtGames:
    print(f"You were either smart, lucky, or good at games, so you're going to be successful in life, {'young' if isYoung else 'old'} one.")
elif isYoung:
    print("You were not smart, lucky, or good at games, but you're young. That means you have time to get better. Good luck young one!")
else:
    print("You're old, and you're not good at games, you're not smart, and you're not lucky eiter. Well, I wish you luck (because you don't have any).")
    
