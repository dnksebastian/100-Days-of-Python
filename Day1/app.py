#print("Hello world!") #prints the string into the console

#print("Day 1 - Python Print Function")
#print("The function is declared like this:")
#print("print('what to print')") #single quotes are used here to avoid syntax error

# How to print multiple line strings within single print call:

#print("Hello world!\nHello world!\nHello world!") #using \n

#Concatenating (combining) strings:

#print("Hello" + " " + "Name") #adding a space with a seperate string

#Debugging - fixing errors: (task)


#Input function:
#input() will get user input in console, then print() will print the word "Hello" and user input!

#print("Hello " + input("What is your name?") +"!")


#Another exercise: print the number of characters in user's name:

#print("The number of characters in your name is: " + str(len(input('What is your name?'))))


#Python variables:

# name = input("What is your name? ")
# print(name)
# length = len(name)
# print(length)


#Another challenge: write a program that switches the values of given variables:

#a = input("a: ")
#b = input("b: ")

#my solution:

#c = a
#a = b
#b = c

####

#print("a = " + a)
#print("b = " + b)


#Naming variables:
#make your code readable - avoid single letters, write self-commenting code
#no spaces between words in variable names - use snake_case



# FINAL PROJECT OF THE DAY - BAND NAME GENERATOR

#1. Create a greeting for yout program
print("This is Band Name Generator!")
#2. Ask the user for the city that they grew up in.
user_city = input("What is the city you grew up in?\n")
#3. Ask the user for the name of a pet.
user_pet = input("What is your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band's name is: " + user_city + " " + user_pet)
#5. Make sure the input cursor shows on a new line.