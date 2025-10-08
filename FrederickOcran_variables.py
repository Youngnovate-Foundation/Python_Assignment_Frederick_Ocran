# Variables For My Information
myName = "Frederick Ocran"
myAge = 23
myFavLan = "Python and Django"
workDone = True
print ("My name is " + myName + ", I am " + str(myAge) + " years old")
print ("My favorite programming languages are " + myFavLan)
print ("I have done my assignment: " + str(workDone) + "\n")


# Number Variables

num1 = 15
num2 = 4
print ("The sum of " + str(num1) + " and " + str(num2) + " is: " + str(num1 + num2))
print ("The difference of " + str(num1) + " and " + str(num2) + " is: " + str(num1 - num2))
print ("The product of " + str(num1) + " and " + str(num2) + " is: " + str(num1 * num2))
print ("The division of " + str(num1) + " and " + str(num2) + " is: " + str(num1 / num2) + "\n")

# Name Variable
first_name = "Frederick"
last_name = "Ocran"
full_name = first_name + " " + last_name
print ("My full name is " + full_name)
print ("My full name in uppercase is " + full_name.upper())
print (f"Hello! My name is {full_name}, I am learning Python programming.\n")


# User Input
user_name = input("Enter your name: ")
user_food = input("Enter your favorite food: ")
user_rate = input("How many times do you eat it per week?: ")
print (f"Hello {user_name}, you eat {user_food} and {user_rate} times a week.\n")

# Finding Errors
age = 25
height = 5.8
print ("I am " + str(age) + " years old and I am " + str(height) + " feet tall.\n")


# Simple Calculator
num1 = float(input("Enter temperature in Celsius: "))
num2 = (num1 * 9/5) + 32
print (f"The temperature in Fahrenheit is: {num2}°F and the temperature in Celsius is: {num1}°C")