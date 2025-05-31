import random
print("Let's play Rock, Paper, Scissors!")
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rock_paper_scissors = [rock, paper, scissors]
player_choice = input("What do you choose? Type R for Rock, P for Paper and S for Scissors.\n").lower()
if player_choice == "r":
    print(rock_paper_scissors[0])
elif player_choice == "p":
    print(rock_paper_scissors[1])
elif player_choice == "s":
    print(rock_paper_scissors[2])
else:
    print("Choose correctly!")

print("Computer choose:")
computer_choice = random.choice(rock_paper_scissors)
print(computer_choice)

if player_choice == "r":
    if computer_choice == rock_paper_scissors[0]:
        print("It's A DRAW!")
    elif computer_choice == rock_paper_scissors[1]:
        print("COMPUTER WINS!")
    else:
        print("YOU WIN!")

elif player_choice == "p":
    if computer_choice == rock_paper_scissors[0]:
        print("YOU WIN!")
    elif computer_choice == rock_paper_scissors[1]:
        print("It's A DRAW!")
    else:
        print("COMPUTER WINS!")

elif player_choice == "s":
    if computer_choice == rock_paper_scissors[0]:
        print("COMPUTER WINS!")
    elif computer_choice == rock_paper_scissors[1]:
        print("YOU WIN!")
    else:
        print("It's A DRAW!")