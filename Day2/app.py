#Python primitive data types

#Data types:

#Strings - a string of characters - "random string"
#"Hello"[0] - returns "H" - this is called subscripting

#print("Hello[0]")


#Integer - whole numbers (without decimal places)

#print(123 + 345)

#we can divide big numbers with underscore: 123456 = 123_456 (for readibility)

#Float - numbers with decimal places

#3.1456435

#Boolean - only has 2 possible values: True and False


#type() - checks the type of given data

#Type casting - or type conversion

#num_char = len(input("What is your name?\n"))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters")

#a = 123
#print(type(a))

#b = str(a)
#print(b)

#c = float(123)

#print(70 + float("100.5"))
#print(str(70) + str(100))



################# Coding Exercise ##############
#add the digits from a two digit number given by user:
#Example: 39 = 3 + 9 = 12

#two_digit_number = input("Type a two digit number:\n")

#### Solution:

#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])

#result = first_digit + second_digit
#print(result)

################################################
#Mathematical operators:
#3 + 5
#7 - 3
#3 * 2
#6 / 2 - always gives a float
#8 // 3 - floored division, gives int
#2 ** 3 - exponent

#Priority: PEMDAS

################################################
##Coding exercise: BMI calculator
#bmi formula = weight / height^2
#don't change the code below
#height = input("Enter your height in m: \n")
#weight = input("Enter your weight in kg: \n")

## solution:
#height_num = float(height)
#weight_num = float(weight)

#bmi_result = round(weight_num / height_num**2)

#print(bmi_result)


####### f-strings
#score = 0
#height = 1.8
#isWinning = True
#f"your score is {score}, your height is {height}, you are winning is {isWinning}"

############ Coding challange:##########################
#Create a program using maths and fStrings that tells us how many days, weeks, months we have left if we live until 90 years old. 
# Take current age as input and output a message like this: "You have x days, y weeks, and z months left."
#assume 1 year = 365 days, 52 weeks and 12 months

#age = input("What is your current age? \n")

#age_int = int(age)
#years_left = 90 - age_int
#age_months = years_left * 12
#age_weeks = years_left * 52
#age_days = years_left * 365

#result = f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left."
#print(result)


####################### Final project of the day: Tip calculator ##########################################
print("Welcome to the tip calculator.")
user_bill = input("What was the total bill?\n$")
user_tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
user_people = input("How many people to split the bill?\n")

user_bill_float = float(user_bill)
user_tip_float = 1 + int(user_tip) / 100
user_people_int = int(user_people)

result = user_bill_float * user_tip_float / user_people_int
result_rounded = round(result, 2)

print(f"Each person should pay: ${result_rounded}")