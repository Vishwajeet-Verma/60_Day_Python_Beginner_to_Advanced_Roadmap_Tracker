# DAY 04 — PYTHON FUNDAMENTALS


# Today's Lesson

# Type Casting & User Input


# Aaj kya seekhenge?

# - input() function
# - print() function
# - Type casting: int(), float(), str(), bool()
# - Implicit vs Explicit Type Casting
# - User input ke saath calculations
# - ValueError aur basic input validation




# 1. User Input kya hota hai?
# Abhi tak hum Python mein values khud code ke andar likhte the.

# Example:

# name = "Vashu"
# age = 19

# print(name)
# print(age)


# Ismein user apni taraf se koi information enter nahi kar sakta.

# Lekin real-world applications mein user se information leni padti hai.

# Examples:
# - Login system mein username aur password.
# - Registration form mein name, email aur age.
# - Calculator mein numbers.
# - Cybersecurity tool mein IP address ya port number.

# Python mein user se input lene ke liye input() function use hota hai.

# 2. input() Function

# Syntax:

# variable = input("Message")

# Example:

# name = input("Enter Your Name: ")
# print("Welcome", name)

# Output:
# Enter your name: Vashu
# Welcome Vashu


# Samjho code mein kya hua:

# 1. input() user ko message show karta hai.
# 2. Program user ke input ka wait karta hai.
# 3. User jo value enter karta hai, Python use variable mein store kar deta hai.
# 4. print() us value ko display karta hai.


# Important Rule

# input() function hamesha user ke input ko string (str) ke form mein return karta hai.

# Example:

# age = input("Enter your age: ")

# print(age)
# print(type(age))

# Output:
# Enter your age: 19
# 19
# <class 'str'>

# Dhyan dena: User ne 19 enter kiya, lekin Python ne use string "19" ke roop mein store kiya.

# Yahin se Type Casting ki zarurat padti hai.


# 3. Type Casting kya hoti hai?

# Type Casting ka matlab hai ek data type ko doosre data type mein convert karna.

# Example:

# - String → Integer
# - Integer → Float
# - Float → Integer
# - Integer → String

# Python mein Type Casting ke liye built-in functions available hain.

# Function	    Conversion

# int()	        Integer
# float()	    Float
# str()	        String
# bool()	    Boolean


# 3.1 String to Integer — int()


# number = "100"

# converted = int(number)

# print(converted)
# print(type(converted))

# Output:
# 100   
# <class 'int'>



# Explanation:

# - number ek string hai.
# - int(number) string ko integer mein convert karta hai.
# - converted mein integer value store hoti hai.

# Ab tum integer par mathematical operations kar sakte ho.


# a = "50"
# b = "20"

# result = int(a) + int(b)

# print(result)

# Output:
# 70

# Agar tum int() use nahi karte, toh + operator strings ko join karega:

# a = "50"
# b = "20"
# 
# print(a + b)

# Output:
# 5020

# Difference: String addition mein concatenation hota hai, jabki integer addition mein mathematical calculation hoti hai.


# 3.2 String to Float — float()

# Jab decimal number ko convert karna ho, tab float() use karte hain.


# price = "99.50"

# converted_price = float(price)

# print(converted_price)
# print(type(converted_price))


# Output:
# 99.5
# <class 'float'>


# # Practical example:


# price = input("Enter product price: ")

# quantity = input("Enter quantity: ")

# total = float(price) * int(quantity)

# print("Total Price:", total)



# 3.3 Integer to String — str()

# Jab integer ko string mein convert karna ho, toh str() use hota hai.

# age = 19

# converted_age = str(age)

# print(converted_age)
# print(type(converted_age))

# Output:
# 19
# <class 'str'>


# # Example:

# age = 19

# message = "My age is " + str(age)

# print(message)


# Output:
# My age is 19


# 3.4 Integer to Float


# number = 10

# result = float(number)

# print(result)
# print(type(result))

# Output:
# 10.0
# <class 'float'>


# 3.5 Float to Integer

# number = 10.85

# result = int(number)

# print(result)

# Output:
# 10

# Important
#  int() decimal ko round off nahi karta. Ye decimal ke baad ka part remove kar deta hai.

# For example:


# 4. Implicit vs Explicit Type Casting

# Python mein Type Conversion ke do important types hote hain.

# 4.1 Implicit Type Casting

# Jab Python khud ek compatible data type ko doosre data type mein convert karta hai, use Implicit Type Casting kehte hain.

# Example:

# a = 10
# b = 5.5

# result = a + b

# print(result)
# print(type(result))

# Output:
# 15.5
# <class 'float'>

# Yahan:
# - a integer hai.
# - b float hai.
# - Python calculation ke liye integer ko float mein convert kar deta hai.




# 4.2 Explicit Type Casting

# Jab programmer khud conversion karta hai, use Explicit Type Casting kehte hain.

# Example:

# age = "20"

# age = int(age)

# print(age)
# print(type(age))

# Output:
# 20
# <class 'int'>


# Implicit	                            Explicit

# Python khud convert karta hai	        Programmer convert karta hai
# Automatic conversion	                Manual conversion
# Example: 10 + 5.5	                    Example: int("20")


# 5. User Input + Type Casting Together

# Ab dono concepts ko combine karte hain.

# # Example 1: Age Calculator

# name = input("Enter your name: ")

# age = int(input("Enter your age: "))

# future_age = age + 5

# print("Hello", name)
# print("Your current age:", age)
# print("Your age after 5 years:", future_age)


# Output:
# Enter your name: Vashu
# Enter your age: 19

# Hello Vashu
# Your current age: 19
# Your age after 5 years: 24


# Example 2: Simple Calculator

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# print("Addition:", addition)
# print("Subtraction:", subtraction)
# print("Multiplication:", multiplication)
# print("Division:", division)


# Output:
# Enter first number: 20
# Enter second number: 10

# Addition: 30.0
# Subtraction: 10.0
# Multiplication: 200.0
# Division: 2.0


# Note: Is example mein second number 0 hua toh division error aayega. Isko hum aage input validation ke through handle karenge.


# 6. bool() Type Casting

# Python mein bool() kisi value ko Boolean (True ya False) mein convert karta hai.

# Example:

# print(bool(1))
# print(bool(0))

# print(bool("Hello"))
# print(bool(""))

# Output:
# True
# False
# True
# False


# Important rules:


# Value	        Boolean Result

# 0	            False
# 1	            True
# ""	        False
# "Hello"	    True
# []	        False
# [1, 2]	    True
# None	        False

# Yaad rakho: Empty values generally False hoti hain, aur non-empty values generally True hoti hain.


# 7. Common Errors in Type Casting

# Type Casting karte waqt invalid input dene par error aa sakta hai.

# Example:

# age = int("hello")

# print(age)

# Output:
# ValueError: invalid literal for int()

# Kyun?

# Kyunki "hello" ko integer mein convert nahi kiya ja sakta.
# Error Handling with try-except

# try:
#     age = int(input("Enter your age: "))

#     print("Your age is:", age)

# except ValueError:
#     print("Please enter a valid number!")

# Output with valid input:
# Enter your age: 19
# Your age is: 19


# Output with invalid input:
# Enter your age: hello
# Please enter a valid number! 


# Ye basic input validation hai. Real-world applications mein user input ko validate karna bahut important hota hai.



# 8. Mini Project — Student Information System

# Ab hum aaj ke concepts ko ek mini project mein apply karenge.
# Practice Project
# Project: Student Information System

# print("===== STUDENT INFORMATION SYSTEM =====")

# name = input("Enter your name: ")
# roll_number = int(input("Enter your roll number: "))
# age = int(input("Enter your age: "))
# course = input("Enter your course: ")
# percentage = float(input("Enter your percentage: "))

# print("\n===== STUDENT DETAILS =====")

# print("Name:", name)
# print("Roll Number:", roll_number)
# print("Age:", age)
# print("Course:", course)
# print("Percentage:", percentage)

# Sample Output:
# ===== STUDENT INFORMATION SYSTEM =====
# Enter your name: Vashu
# Enter your roll number: 493
# Enter your age: 83
# Enter your course: BCA
# Enter your percentage: 93.03

# ===== STUDENT DETAILS =====
# Name: Vashu
# Roll Number: 493
# Age: 83
# Course: BCA
# Percentage: 93.03



# Is project mein tumne use kiya:

# - input() — User se information lena.
# - int() — Roll number aur age convert karna.
# - float() — Percentage convert karna.
# - print() — Student details display karna.



# 9. Practical Assignments
# Ab tumhari actual practice shuru hoti hai. In assignments ko khud VS Code mein solve karna.



# Task 1: User Introduction Program

# User se name, age aur city input lo aur ek introduction print karo.


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your City: ")

# print("Your name is: ", name)
# print("Your age is: ", age)
# print("Your city is: ", city)



# Task 2: Age Calculator

# User ki current age lo aur 10 years baad ki age calculate karo.


# name = input("Enter your Name: ")
# age = int(input("Enter your Age: "))
# future_age = age + 10

# print("Hello", name)
# print("Your Current Age is: ", age)
# print("Your age after 10 Year: ", future_age)




# Task 3: Simple Calculator

# Do numbers input lo aur addition, subtraction, multiplication aur division perform karo.


# num1 = int(input("Enter your first Number: "))
# num2 = int(input("Enter your second Number: "))

# addition =  num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# print("Your First number is: ", num1)
# print("Your Second number is: ", num2)
# print("Addition : ", addition)
# print("Subtraction :", subtraction)
# print("Multiplicaiton : ", multiplication)
# print("Division : ", division)


