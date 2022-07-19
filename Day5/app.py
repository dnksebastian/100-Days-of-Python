#Loops, range and code blocks

#for item in list_of_items

#fruits = ["Apple", "Peach", "Pear"]

#for fruit in fruits:
#    print(fruit)

 ############ Coding exercise
# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Don't change the code below 
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# Don't change the code above 


#Write your code below this row 

# print(student_heights)

# count = 0
# summ = 0
# for num in student_heights:
#     count += 1
#     summ += num

# average = round(summ / count)
# print(average)

################course solutuion:
# total_height = 0
# number_of_students = 0

# for student in student_heights:
#     number_of_students += 1

# for height in student_heights:
#     total_height += height

# average_height = round(total_height / number_of_students)
# print(average_height)



######################################## coding exercise 

# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

# Don't change the code below
# from re import S


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# Don't change the code above

#Write your code below this row 

# current_num = 0
# bigger_num = 0

# for num in student_scores:
#     if num >= current_num:
#         current_num = num
    
#     if current_num >= bigger_num:
#         bigger_num = current_num

# print(f"The highest score is: {bigger_num}")


#### Course solutuion:

# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")



################ for loops and the range() function

# for number in range(1, 11):
#     print(number)


# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

############################################ Coding exercise:
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

#Solution:

# total = 0
# for number in range(2, 101, 2):
#     total += number

# print(total)

############ alternative

# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number

# print(total)

###################################### coding exercise
# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`


##### Solution:

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


############################### Final project of the day:
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

counter = 0
letter_sample = ""

for letter in letters:
    if counter < nr_letters:
        letter_sample += str(letters[random.randint(0, len(letters) - 1)])
        counter += 1

counter2 = 0
numbers_sample = ""
for number in numbers:
    if counter2 < nr_numbers:
        numbers_sample += str(numbers[random.randint(0, len(numbers) - 1)])
        counter2 += 1

counter3 = 0
symbols_sample = ""
for symbol in symbols:
    if counter3 < nr_symbols:
        symbols_sample += str(symbols[random.randint(0, len(symbols) - 1)])
        counter3 += 1

password_final = letter_sample + symbols_sample + numbers_sample
print(f"Here is your password: {password_final}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_final_copy = list(password_final)
pwd_final_shuffle = random.shuffle(password_final_copy)
pwd_final = "".join(password_final_copy)

print(f"Here is your shuffled password: {pwd_final}")


# ########### Course solution:
# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")