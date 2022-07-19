#Importing modules:
import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

############ Coding exercise:
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails

# random_num = random.randint(0, 1)

# if random_num == 0:
#     print("Heads")
# else:
#     print("Tails")


### Python lists:
# Way of storing data in Python

# fruits = [item1, item2]

# fruits = ["Apple", "Orange", "Banana"]

############## Coding exercise:
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Split string method

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# #Don't change the code above

# #Solution
# random_position = random.randint(0, len(names) - 1)
# chosen_name = names[random_position]
# print(f"{chosen_name} is going to buy the meal today!")



########## Coding exercise
# You are going to write a program which will mark a spot with an X.
# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# First your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".

#  Don't change the code below 
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # Don't change the code above 

# #Write your code below this row 

# col = int(position[0]) - 1
# row = int(position[1]) - 1

# map[row][col] = "X"

# #Write your code above this row

# # 🚨 Don't change the code below
# print(f"{row1}\n{row2}\n{row3}")


############################### Final project of the day
##### Rock, paper, scissors
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line:

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


random_computer_choice = random.randint(0, 2)

###### Player chose rock ######
if player_choice == "0" and random_computer_choice == 0:
    print(rock)
    print("Computer chose:")
    print(rock)
    print("It's a draw!")
elif player_choice == "0" and random_computer_choice == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose")
elif player_choice == "0" and random_computer_choice == 2:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win")

###### Player chose paper ######
elif player_choice == "1" and random_computer_choice == 0:
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win")
elif player_choice == "1" and random_computer_choice == 1:
    print(paper)
    print("Computer chose:")
    print(paper)
    print("It's a draw!")
elif player_choice == "1" and random_computer_choice == 2:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose")

###### Player chose scissors ######    
elif player_choice == "2" and random_computer_choice == 0:
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose")
elif player_choice == "2" and random_computer_choice == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win")
elif player_choice == "2" and random_computer_choice == 2:
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("It's a draw!")
else:
    print("Please choose a valid option. Type 0 for Rock, 1 for Paper or 2 for Scissors.")




##### Course solution:

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# if user_choice >= 3 or user_choice < 0:
#     print("You typed and invalid number, you lose!")
# else:

#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)


#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose!")
#     elif computer_choice > user_choice:
#         print("You lose!")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw!")