# Variables, Constants & Naming Rules


# PART 1 – Understanding Variables

# 1. What is a Variable?
# Variable ek named reference hota hai jiske through hum program mein data ko store aur access kar sakte hain.

# Simple example:

# name = "Vishwajeet"
# age = 20
# course = "BCA"



# Yahan:

# - name ek variable hai.
# - age ek variable hai.
# - course ek variable hai.

# In variables mein humne different types ka data assign kiya hai.


# Real-life example:

# Socho ek college student ka record hai:

# Variable	    Stored Value

# name  	    Vishwajeet
# age	        20
# course	    BCA
# semester	    1

# Python mein:
# name = "Vishwajeet"
# age = 20
# course = "BCA"
# semester = 1

# print(name)
# print(age)
# print(course)
# print(semester)


# Output:

# Vishwajeet
# 20
# BCA
# 1




# 2. How Variables Work Internally

# Python mein variable ko samajhne ka ek useful way hai: variable ek object ko refer karta hai.

# Example:

# x = 100


# Iska matlab hai ki Python integer object 100 create karta hai aur x ko us object ka reference deta hai.


# Variable Reference Visualization

# Variable name
#       x

#       ↓

# References to

# Integer Object
#     100
#     int


# Python mein variables ko traditional boxes samajhna ek beginner-friendly analogy hai, lekin technically variables objects ke references/names hote hain.



# 3. Variable Assignment

# Variable mein value assign karne ke liye = assignment operator use hota hai.

# username = "admin"
# password_length = 12
# is_logged_in = True



# Yahan:

# - username → variable name
# - = → assignment operator
# - "admin" → assigned value

# Important: = ka meaning mathematics wala equal-to nahi hota. Python mein ye assignment karta hai.

# Comparison:
# x = 10       # Assignment
# x == 10      # Comparison



# == check karta hai ki dono values equal hain ya nahi.




# 4. Variable Reassignment

# Python mein kisi existing variable ki value change kar sakte hain.

# score = 50
# print(score)
# 
# score = 80
# print(score)



# Output:
# 50
# 80


# Yahan score pehle 50 refer kar raha tha, baad mein 80 refer karne laga.




# 5. Dynamic Typing in Python

# Python ek dynamically typed language hai.

# Iska matlab hai ki tumhe variable ka data type declare karne ki zarurat nahi hoti. Python runtime par object ka type identify karta hai.

# Example:

# data = 100
# print(type(data))

# data = "Python"
# print(type(data))

# data = 10.5
# print(type(data))



# Output:
# <class 'int'>
# <class 'str'>
# <class 'float'>


# Notice karo, same variable data different types ke objects ko refer kar raha hai.

# Important: Python dynamically typed hai, lekin strongly typed bhi hai. Matlab incompatible types ko automatically har situation mein convert nahi karta.

# Example:

# age = 20
# name = "Vishwajeet"
# print(age + name)


# Output:
# TypeError

# Kyunki integer aur string ko directly add nahi kar sakte.





# PART 2 – Types of Variables

# 6. Variables Based on Data

# Python variables different types ka data hold kar sakte hain.

# Data Type	    Example

# Integer	    age = 20
# Float	        price = 99.50
# String	    name = "Python"
# Boolean	    is_active = True
# List	        skills = ["Python", "Linux"]
# Tuple	        coordinates = (10, 20)
# Dictionary	user = {"name": "Vishwajeet"}
# Set	        numbers = {1, 2, 3}


# Example: 

# name = "Vishwajeet"
# age = 20
# percentage = 85.5
# is_student = True
# skills = ["Python", "Linux", "Networking"]

# print(type(name))
# print(type(age))
# print(type(percentage))
# print(type(is_student))
# print(type(skills))

# type() function ka use kisi object ka data type check karne ke liye hota hai.






# 7. What is a Constant?
# Constant ek aisa named value hota hai jise program ke dauran change nahi karna chahiye.

# Example:

# PI = 3.14159
# MAX_LOGIN_ATTEMPTS = 3
# APP_NAME = "Secure Login System"


# Yahan:
# - PI mathematical constant hai.
# - MAX_LOGIN_ATTEMPTS maximum login attempts represent karta hai.
# - APP_NAME application ka naam represent karta hai.

# Important Python concept:

# Python mein C, C++ ya Java ki tarah built-in const keyword nahi hota.

# Python mein constants convention ke through represent kiye jaate hain. Convention hai: variable name ko uppercase mein likhna.

# Example:
# MAX_USERS = 100
# print(MAX_USERS)



# Lekin technically Python mein tum ise change kar sakte ho:

# MAX_USERS = 100
# MAX_USERS = 200
# print(MAX_USERS)



# Output:
# 200


# Isliye uppercase naming ek convention hai, strict enforcement nahi.





# 8. Variables vs Constants

# Variables	            Constants

# Values may change	    Values should not change
# Usually lowercase	    Usually uppercase
# username	            MAX_USERS
# score = 50	        PI = 3.14159


# Real-world example:

# #Constants
# MAX_ATTEMPTS = 3
# APP_NAME = "Secure Login"

# # Variables
# username = "admin"
# login_attempts = 0
# login_attempts = login_attempts + 1

# print(APP_NAME)
# print(username)
# print(login_attempts)



# PART 4 – Python Naming Rules

# 9. What is an Identifier?
# Identifier kisi bhi variable, function, class ya other named object ko diya gaya naam hota hai.

# Example:
# student_name = "Vishwajeet"



# Yahan student_name identifier hai.

# Python mein identifiers ke liye kuch strict rules hain.


# 10. Seven Important Naming Rules

# Rule 1: Names can contain letters.

# name = "Python"
# student = "Vishwajeet"



# Rule 2: Numbers allowed hain, lekin starting mein nahi
# .
# student1 = "Aman"     # Valid
# name2026 = "Python"   # Valid



# Invalid:
# 1student = "Aman"



# Rule 3: Underscore allowed hai.

# student_name = "Aman"
# user_password = "12345678"



# Rule 4: Spaces allowed nahi hain.

# Invalid:
# student name = "Aman"



# Correct:
# student_name = "Aman"



# Rule 5: Special characters allowed nahi hain.

# Invalid:
# user@name = "admin"
# user-name = "admin"



# Correct:
# user_name = "admin"



# Rule 6: Python keywords ko variable name nahi bana sakte.

# Invalid:
# if = 10
# class = "BCA"
# for = 20



# Rule 7: Python is case-sensitive.

# name = "Vishwajeet"
# Name = "Aman"
# NAME = "Rahul"

# print(name)
# print(Name)
# print(NAME)



# Ye teeno different identifiers hain.


# 11. Python Keywords

# Keywords Python ke reserved words hote hain jo language ke specific purpose ke liye reserved hain.

# Examples:

# if, else, elif, for, while, class, def, return, import, True, False, None.

# Python mein keywords ki list check karne ke liye:

# import keyword
# print(keyword.kwlist)



# Total keyword count check karne ke liye:
# import keyword
# print(len(keyword.kwlist))



# Isse tumhare installed Python version ke according keyword count milega.



# PART 5 – Naming Conventions

# Naming rules aur naming conventions mein difference samajhna bahut important hai.

# - Rules: Follow karna compulsory hai, warna SyntaxError ho sakta hai.
# - Conventions: Recommended coding practices hain, taaki code readable rahe.


# 12. Python Naming Styles

# Style	        Example	        Common Usage

# snake_case	student_name	Variables, functions
# PascalCase	StudentRecord	Classes
# UPPER_CASE	MAX_LIMIT	    Constants

# camelCase	studentName	Less common in Python

# Recommended
#  Python mein variables aur functions ke liye snake_case use karo.

# Example:
# student_name = "Vishwajeet"
# total_marks = 450
# login_attempts = 3



# Avoid:
# StudentName = "Vishwajeet"
# totalMarks = 450
# x = 3



# x technically valid hai, lekin meaningful variable names code ko zyada readable banate hain.



# PART 6 – Multiple Assignment

# 13. Assign Multiple Variables in One Line

# Python mein ek hi line mein multiple variables assign kar sakte ho.

# name, age, course = "Vishwajeet", 20, "BCA"

# print(name)
# print(age)
# print(course)


# Output:
# Vishwajeet
# 20
# BCA


# 14. Assign Same Value to Multiple Variables

# a = b = c = 100
# print(a)
# print(b)
# print(c)


# Output:
# 100
# 100
# 100


# Teeno names same integer object ko refer karte hain.


# 15. Variable Swapping

# Python mein bina temporary variable ke do variables ki values exchange kar sakte hain.

# a = 10
# b = 20
# a, b = b, a

# print(a)
# print(b)



# Output:
# 20
# 10


# Ye Python ki powerful unpacking technique hai.



# PART 7 – Advanced Understanding

# Ab kuch aise concepts samajhte hain jo tumhari Python fundamentals ko aur strong banayenge.

# 16. Understanding id() Function

# Python mein id() function kisi object ki identity return karta hai.

# a = 100
# b = 100
# print(id(a))
# print(id(b))



# Dono IDs same aa sakti hain, kyunki Python kuch immutable objects ko internally reuse kar sakta hai. Is behavior ko implementation details ke roop mein samajhna chahiye.

# Ek aur example:

# x = "Python"
# print(id(x))

# x = "Cybersecurity"
# print(id(x))

# Yahan x ab ek different string object ko refer kar sakta hai.


# 17. Variable vs Object Mutability

# Python mein objects do broad categories mein samajhe ja sakte hain:

# - Mutable: Object ki contents change ki ja sakti hain.
# - Immutable: Object ki contents change nahi ki ja sakti.

# Mutable	    Immutable
# List	        Integer
# Dictionary	Float
# Set	        String
#	            Tuple
# 

# Example:

# Mutable object
# skills = ["Python", "Linux"]skills.append("Networking")print(skills)

# Output:
# ['Python', 'Linux', 'Networking']


# Ab immutable example:

# name = "Python"
# name = name + " Programming"
# print(name)


# Output:
# Python Programming


# Yahan original string modify nahi hui. Ek new string object create hua aur name usse refer karne laga.


# 18. Variable Scope – Introduction
# Variable scope ka matlab hai ki program ke kis part mein variable accessible hai.

# Do important scopes:

# Global variable:

# username = "admin"
# def show_user():
#     print(username)
#     show_user()



# Local variable:

# def login():
#     attempts = 3    
#     print(attempts)
# login()



# Yahan attempts function ke andar defined hai, isliye ye local variable hai.

# Scope ko hum Day 2 mein introduce kar rahe hain. Iska detailed explanation functions wale day mein karenge.




# PART 8 – Real-World Cybersecurity Example


# Ab ek chhota practical example banate hain jisme variables aur constants use honge.

# Secure Login Configuration

    
# # Application Constants
# APP_NAME = "Secure Login System"
# MAX_LOGIN_ATTEMPTS = 3
# MIN_PASSWORD_LENGTH = 8

# # User Variables
# username = "admin"
# password = "Secure@123"
# login_attempts = 1

# # Display Information
# print("Application:", APP_NAME)
# print("Username:", username)
# print("Password Length:", len(password))
# print("Login Attempts:", login_attempts)

# # Basic Checks
# # 
# if len(password) >= MIN_PASSWORD_LENGTH:
#     print("Password Length: Valid")
# else:
#     print("Password Length: Invalid")

# if login_attempts <= MAX_LOGIN_ATTEMPTS:
#     print("Login Attempts: Within Limit")

# else:    print("Login Attempts: Exceeded")



# Output:
# Application: Secure Login System
# Username: admin
# Password Length: 10
# Login Attempts: 1
# Password Length: Valid
# Login Attempts: Within Limit


# Cybersecurity lesson: Real applications mein passwords ko plain text mein store ya logs mein print nahi karna chahiye. Ye example sirf variables aur conditions practice karne ke liye hai.



# PART 9 – Practical Assignments

# Ab tumhari coding practice start hoti hai.

# Day 02 Practical Work

# Task 1 – Student Information System

# Variables use karke student information store karo.

# Requirements:

# - Student name
# - Roll number
# - Course
# - Semester
# - College name
# - Is student active?


# Expected output:

# ========== STUDENT PROFILE ==========

# Name: Vishwajeet 
# Roll Number: 12345678
# Course: BCA
# Semester: 1
# College: DSVV
# Active Student: True

# =====================================

# My Practice.. 

# sutdent_name = "Vishwajeet"
# rool_no = 12345678
# course = "BCA"
# sem = 1
# college_name = "DSVV"
# is_active = True

# print("Student Name: ", sutdent_name)
# print("Roll Number: ", rool_no)
# print("Course : ", course)
# print("Semester : ", sem)
# print("Colllege : ", college_name)
# print("Actuve Student : ", is_active)




# Task 2 – Constants Practice

# Ek program banao jisme ye constants hon:

# COLLEGE_NAME = "DSVV"
# MAX_ATTEMPTS = 3
# PASSING_MARKS = 40
# APP_VERSION = "1.0"


# In sabhi constants ko print karo.


# Task 3 – Variable Reassignment

# Program banao:
# 1. balance = 1000 assign karo.
# 2. Balance mein 500 add karo.
# 3. Balance se 200 subtract karo.
# 4. Final balance print karo.

# Expected output:

# Initial Balance: 1000
# After Deposit: 1500
# After Withdrawal: 1300
# Final Balance: 1300


# My Practice

# balance = 1000
# balance = balance + 500
# balance = balance - 200

# print(balance)

