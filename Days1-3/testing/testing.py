# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))

#Inputs!
# firstName = "Dahriel"
# lastName = input("What is your last name?\n")
# lastName = lastName.lower().capitalize()
# print("Hello " + firstName + " my last name is " + lastName + " too!")

# age = input("How old are you?\n")
# age = int(age)
# newage = (age + 3)
# print("In three year's you'll be " + str(newage) + " years old")
# print("That's " + str(newage*7) + " in dog years!")






#Control Flow
# number = input("What's your favorite number? ")
# try:
    

# if int(number)%2 == 0:
#     print("Your number is even!\n")
# else:
#     print("Your number is odd!\n")

score = 0 
print("This survey will tell you if you should move somewhere warmer")
Q1 = input("Do you like swimming out doors?\n")
if Q1 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q2 = input("Do you enjoy sunlight?\n")
if Q2 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q3 = input("Do you find long or heavy clothing uncomfortable?\n")
if Q3 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q4 = input("Do you like icecream?\n")
if Q4 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q5 = input("Are you ok with a few bugs in the air?\n")
if Q5 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q6 = input("Can you handle any heat?\n")
if Q6 == "yes":
     score = score + 1
else:
    score = score - 1
print(score)

Q7 = input("Do you like snow?\n")
if Q7 == "no":
     score = score + 1
else:
    score = score - 1
print(score)

if score > 0:
    print("You should go somewhere warmer. Maybe the carribean?")
else:
    print("Good luck getting through this summer")






