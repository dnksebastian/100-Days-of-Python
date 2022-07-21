########## Functions

#keyword: def
# def my_function():
#   print("Hello")
#   print("Bye")

#my_function() - calling the function

#Solution o Reeborg.ca Hurdle 1 exercise:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def run(x):
#     for hurdle in range(x):
#         move()
#         jump()

# run(6)


########## while loops
#while something_is_true
    #do something repetedly

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1

####### Problem of infinite loops

########## reborg.ca hurdle 3 solution:
# while at_goal() != True:
#     if front_is_clear() == True:
#         move()
#     if wall_in_front() == True:
#         jump()

####### reborg.ca Hurgle 4 solution:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear() == True:
#         move()
#     if wall_in_front() == True:
#         turn_left()
#     while is_facing_north() == True:
#         if wall_on_right() == True:
#             move()
#         else:
#             turn_right()
#             move()
#             turn_right()

####### final project of the day:
#reborg.ca maze solution

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if front_is_clear() == True and wall_on_right() == True:
#         move()
#     elif right_is_clear() == True:
#         turn_right()
#         move()
#     else:
#         turn_left()


## Course solution:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


#edge-case code:

# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()

        
# loop = 0  

# while not at_goal():
#      if right_is_clear() and loop < 4:
#          turn_right()
#          move()
#          loop += 1
#      elif front_is_clear():
#          move()
#          loop = 0
#      else:
#          turn_left()
