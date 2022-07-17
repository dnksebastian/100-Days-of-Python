#Conditional statements, logical operators, code blocks and scope

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


#Comparison operators:
#  >, <, >=, <=, ==, !=

################## Coding excercise: ##############
# Write a program that works out wheter if a given number is an odd or even number
#Dont change this line of code:
# number = int(input("Which number do you want to check? \n"))
#Solution:

# if number % 2 != 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")


#Nested if statements


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? \n"))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


############# Coding exercise ############
# Write a program that interprets BMI based on users weight and height.
#It should tell them the interpretation of their BMI based on the value.
# Assume: Under 18.5 they are underweight, over 18.5 but below 25 they have a normal weight, over 25 but below 30 they are overweight, over 30 but below 35 they are obese, above 35 they are clinically obese.
### Don't change code below:
# height = float(input("Enter your height in m: \n"))
# weight = float(input("Enter your weight in kg: \n"))

# #####Solution:

# bmi_res = round(weight / height ** 2)

# if bmi_res < 18.5:
#     print(f"Your BMI is {bmi_res}, you are underweight.")
# elif bmi_res < 25:
#     print(f"Your BMI is {bmi_res}, you have normal weight.")
# elif bmi_res < 30:
#     print(f"Your BMI is {bmi_res}, you are overweight.")
# elif bmi_res < 35:
#     print(f"Your BMI is {bmi_res}, you are obese.")
# else:
#     print(f"Your BMI is {bmi_res}, you are clinically obese.")


############ Coding exercise ###################
# Write a program that check out whether if a given year is a leap year. A normal year has 365 days, leap years have 366 with extra day in February.
# Assume: on every year that is evenly divisible by 4
#           except every year that is evenly divisible by 100
#           unless the year is also evenly divisible by 400
# e.g the year 2000: 2000 / 4 = 500 (leap); 2000 / 100 = 20 (not leap); 2000 / 400 = 5 (leap!)
# but: 2100 / 4 = 525 (leap); 2100 / 100 = 21 (not leap); 2100 / 400 = 5.25 (not leap!)
#Don't change the code below:
# year = int(input("Which year do you want to check? \n"))
###
#Solution:

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")



#Multiple if statements:

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? \n"))
    
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N. \n")
#     if wants_photo == "Y":
#         bill += 3
    
#     print(f"Your final bill is {bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


########## Coding excercise ####################
#Build an automatic pizza order program
#Small Pizza $15
#Medium Pizza $20
#Large Pizza $25
#Pepperoni for small pizza: +$2
#Pepperoni for medium or large pizza +$3
#Extra cheese for any size pizza: +$1

#Dont change anything in lines:
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n")
# add_pepperoni = input("Do you want pepperoni? Y or N. \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")
# #############
# #Solution:
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}.")


#Logical operators:
# A AND B - both have to be true
# C OR D - at least one have to be true
# NOT E - inverse the value

##########################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? \n"))
    
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Midlife crisis tickets are $0.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N. \n")
#     if wants_photo == "Y":
#         bill += 3
    
#     print(f"Your final bill is {bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


################### Coding exercise #######################
# Write a love calculator:
# take both people's names and check for the number of times the letters in the word TRUE occurs, then check for the number of times the letters of word LOVE occurs. Then cobine these numbers to make a 2 digit number.
# For love scores less than 10 or greater than 90 the message should be:
# "Your score is x, you go together like coke and mentos."
# for love scores between 40 and 50 the message should be:
# Your score is y, you are alright together
# Otherwise the messege will just be the score, eg "Your score is z."

#### Dont change these lines of code:
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input ("What is their name? \n")

# ######## Solution:

# helper_string = (name1 + name2).lower()

# count_true = str(helper_string.count("t") + helper_string.count("r") + helper_string.count("u") + helper_string.count("e"))
# count_love = str(helper_string.count("l") + helper_string.count("o") + helper_string.count("v") + helper_string.count("e"))

# result = count_true + count_love
# result_num = int(result)

# if result_num < 10 or result_num > 90:
#     print(f"Your score is {result_num}%, you go together like coke and mentos.")
# elif result_num >= 40 and result_num <= 50:
#     print(f"Your score is {result_num}%, you are alright together")
# else:
#     print(f"Your score is {result_num}%.")


####################### Final project of the day ##############################

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line

player_direction = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if player_direction == "right" or player_direction != "left":
    print("You fell into a hole. Game Over")
else:
    player_decision1 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if player_decision1 == "swim" or player_decision1 != "wait":
        print("You get attacked by an angry trout. Game Over.")
    else:
        player_decision2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if player_decision2 == "red":
            print("It's a room full of fire. Game Over.")
        elif player_decision2 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif player_decision2 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")