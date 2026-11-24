# Day 03 – Data Types



# Today's learning objectives

# - Understand what Data Types are.
# - Learn int, float, str, bool and NoneType.
# - Understand type() and isinstance().
# - Learn type conversion basics.
# - Understand truthy and falsy values.
# - Explore real-world applications.


# PART 1 – What are Data Types?

# 1. Data Type kya hota hai?
# Data Type batata hai ki kisi variable ke through refer kiya gaya data kis category ka hai aur uske saath kis tarah ke operations perform kiye ja sakte hain.

# Example:

# name = "Vashu"
# age = 20
# percentage = 85.5
# is_student = True



# Yahan different types ka data hai:


# Variable	        Value	        Data Type

# name	            "Vashu"	        str
# age	            20	            int
# percentage	    85.5	        float
# is_student	    True	        bool



# Real-life example:

# Socho ek student database hai. Usmein:
 
# - Student name text format mein hoga.
# - Age whole number hogi.
# - Percentage decimal number ho sakta hai.
# - Attendance status True/False ho sakta hai.
# - Middle name unavailable ho toh None ho sakta hai.
# Python mein in sabko represent karne ke liye different data types available hain.


# 2. Python Data Types Overview

# Today's Five Data Types

# 123 
# int
# Whole numbers


# 12.5
# float
# Decimal numbers


# "Hi"
# str
# Text data


# True
# bool
# True / False


# None
# NoneType
# Absence of a value



# PART 2 – Integer (int)

# 3. What is Integer?
# Integer ek numeric data type hai jo whole numbers store karta hai.

# Ismein positive, negative aur zero values aa sakti hain.

# # Examples:

# age = 20
# temperature = -5
# marks = 100
# balance = 0

# print(age)
# print(temperature)
# print(marks)
# print(balance)


# Output:
# 20
# -5
# 100
# 0


# Important: Python integers ki fixed 32-bit ya 64-bit limit nahi hoti. Available memory ke according ye bahut bade integers represent kar sakta hai.

# Integer Mathematical Operations

# a = 20
# b = 10

# print(a + b)   # Addition
# print(a - b)   # Subtraction
# print(a * b)   # Multiplication
# print(a // b)  # Floor division
# print(a % b)   # Modulus
# print(a ** b)  # Exponentiation


# Output:

# 30
# 10
# 200
# 2
# 0
# # 10240000000000

# Yahan:
# - + addition
# - - subtraction
# - * multiplication
# - // floor division
# - % remainder
# - ** power


# Check Integer Data Type

# age = 20
# print(type(age))


# Output:
# <class 'int'>




# PART 3 – Float (float)

# 4. What is Float?
# Float ek numeric data type hai jo decimal numbers represent karta hai.

# Examples:

# percentage = 85.5
# price = 99.99
# temperature = 36.6
# pi = 3.14159

# print(percentage)
# print(price)
# print(temperature)
# print(pi)



# Output:
# 85.5
# 99.99
# 36.6
# 3.14159

# Integer vs Float

# Integer	        Float
# Whole numbers	    Decimal numbers
# 10	            10.5
# -20	            -20.75
# 100	            100.0

# Notice:

# a = 10
# b = 10.0
# 
# print(type(a))
# print(type(b))


# Output:
# <class 'int'>
# <class 'float'>


# Dono ki numerical value mathematically equal ho sakti hai, lekin data types different hain.

# Important: Floating Point Precision
# Python mein kuch decimal calculations exact result nahi deti.

# result = 0.1 + 0.2
# print(result)


# Output:
# 0.30000000000000004


# Aisa floating-point binary representation ki wajah se hota hai.

# Financial calculations mein exact decimal arithmetic ke liye decimal module useful hai.

# from decimal import Decimal
# a = Decimal("0.1")
# b = Decimal("0.2")
# print(a + b)



# Output:
# 0.3




# PART 4 – String (str)

# 5. What is String?
# String ek data type hai jiska use text data store karne ke liye hota hai.

# Python mein string characters ka sequence hoti hai.

# Examples:
# name = "Vishwajeet"
# course = 'BCA'
# message = "Learning Python"



# Strings ko single quotes, double quotes ya triple quotes mein likh sakte hain.


# a = 'Hello'
# b = "Python"
# c = """Welcome to Python Programming"""
# 
# print(a)
# print(b)
# print(c)



# String Operations

# 1. Concatenation

# Do strings ko combine karna concatenation kehlata hai.

# first_name = "Vashu"
# last_name = "Verma"
# full_name = first_name + " " + last_name
# 
# print(full_name)

# Output:
# Vashu Verma


# 2. Repetition

# word = "Python "
# print(word * 3)

# Output:
# Python Python Python


# 3. String Length

# len() function characters ki total count return karta hai.
# language = "Python"
# print(len(language))

# Output:
# 6


# 4. Indexing

# String ke individual characters ko access kar sakte hain.

# language = "Python"
# print(language[0])
# print(language[1])
# print(language[-1])



# Output:
# P
# y
# n


# Python indexing zero se start hoti hai.

# 5. Slicing

# String ka specific part extract kar sakte hain.

# language = "Python"
# print(language[0:3])



# Output:
# Pyt


# String Important Properties
# Python strings immutable hoti hain.

# Matlab existing string ke individual characters ko directly change nahi kar sakte.

# Incorrect:

# name = "Python"
# name[0] = "J"

# Isse TypeError milega.

# Correct:

# name = "Python"
# name = "J" + name[1:]
# 
# print(name)

# Output:
# Jython


# Yahan ek new string create hui hai.


# Useful String Methods

# name = "Vashu verma"
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.replace("verma", "kumar"))



# Output:
# VASHU VERMA
# vashu verma
# Vashu Verma
# Vashu verma
# vashu kumar



# f-Strings

# Python mein strings ke andar variables insert karne ke liye f-strings use kar sakte hain.

# name = "Vashu"
# age = 20
# print(f"My name is {name} and my age is {age}.")



# Output:
# My name is Vashu and my age is 20.


# f-strings real-world applications mein bahut useful hain.



# PART 5 – Boolean (bool)

# 6. What is Boolean?

# Boolean ek data type hai jiske paas sirf do possible values hoti hain:
# - True
# - False
# Boolean ka use conditions, decision-making, authentication aur status checking mein hota hai.

# Example:

# is_student = True
# is_logged_in = False

# print(is_student)
# print(is_logged_in)
# print(type(is_student))



# Output:
# True
# False
# <class 'bool'>


# Important: Python mein True aur False ka first letter capital hota hai.

# Incorrect:
# status = true


# Correct:
# status = True



# 7. Boolean with Comparison Operators

# Boolean values mostly comparison operations se generate hoti hain.

# a = 10
# b = 20

# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)



# Output:
# False
# True
# False
# True
# False
# True


# Operator	Meaning

# >	Greater than
# <	Less than
# ==	Equal to
# !=	Not equal to
# >=	Greater than or equal
# <=	Less than or equal



# 8. Boolean with Logical Operators

# Python mein three important logical operators hote hain:

# - and
# - or
# - not

# AND: Dono conditions True honi chahiye.

# age = 20
# has_id = True
# print(age >= 18 and has_id)


# Output:
# True



# OR: At least one condition True honi chahiye.

# is_admin = False
# is_staff = True
# print(is_admin or is_staff)


# Output:
# True


# NOT: Boolean result ko reverse karta hai.

# is_blocked = False
# print(not is_blocked)


# Output:
# True



# Truth Table

# A	        B	        A and B	    A or B
# True	    True	    True	    True
# True	    False	    False	    True
# False	    True	    False	    True
# False	    False	    False	    False



# PART 6 – NoneType

# 9. What is None?

# Python mein None ek special value hai jo absence of a value ya currently unavailable value ko represent karti hai.

# Example:

# result = None

# print(result)
# print(type(result))



# Output:
# None
# <class 'NoneType'>


# Yahan result variable exist karta hai, lekin usmein abhi meaningful result assign nahi hua hai.


# Real-World Example

# Suppose ek user profile hai jisme phone number abhi available nahi hai.

# username = "vashu"
# phone_number = None
# print(username)
# print(phone_number)



# Output:
# vashu
# None



# Checking None
# None ko check karne ke liye is operator use karna recommended hai.

# phone_number = None

# if phone_number is None:
#     print("Phone number not available")
# else:
#     print("Phone number available")

# Output:
# Phone number not available


# Important: None aur 0 same nahi hain.
# a = None
# b = 0
# print(a == b)



# Output:
# False


# None ek special singleton object hai. Python mein iska type NoneType hai.





# PART 7 – Type Checking

# 10. Using type()

# Ab tak humne type() function multiple examples mein use kiya hai.

# Iska use kisi object ka type identify karne ke liye hota hai.

# a = 100
# b = 10.5
# c = "Python"
# d = True
# e = None

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))



# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'NoneType'>



# 11. Using isinstance()

# isinstance() function check karta hai ki object kisi specified type ya type group ka instance hai ya nahi.

# Example:

# age = 20

# print(isinstance(age, int))
# print(isinstance(age, str))



# Output:
# True
# False


# type() vs isinstance()

# type()	                                        isinstance()

# Exact object's type identify karta hai	        Type membership check karta hai
# type(x)	                                        isinstance(x, int)
# Exact type comparison	                            Inheritance ko bhi consider karta hai

# Ek interesting Python example:

# print(isinstance(True, int))
# print(type(True) == int) 


# Aisa isliye kyunki Python mein bool, int ka subclass hai.

# Ye advanced concept future programming mein useful hoga.



# PART 8 – Type Conversion

# 12. What is Type Conversion?

# Type Conversion ka matlab ek data type ko doosre data type mein convert karna hai.

# Example:

# age = "20"

# age = int(age)

# print(age)
# print(type(age))

# Output:
# 20
# <class 'int'>


# Yahan string "20" integer 20 mein convert hui.

# Python mein common conversion functions:

# Function	Conversion

# int()	    Integer
# float()	    Float
# str()	    String
# bool()	    Boolean


# A. String to Integer

# number = "100"

# converted = int(number)

# print(converted)

# print(type(converted))


# B. Integer to Float

# number = 50

# converted = float(number)

# print(converted)

# Output:
# 50.0

# C. Integer to String

# age = 20

# converted = str(age)

# print(type(converted))

# Output:
# <class 'str'>

# D. Float to Integer

# price = 99.99

# converted = int(price)

# print(converted)

# Output:
# 99

# Notice: int() decimal part ko truncate karta hai, round nahi karta.

# E. Boolean Conversion

# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool("Python"))
# print(bool(None))

# Output:
# True
# False
# False
# True
# False



# PART 9 – Truthy and Falsy Values

# 13. Understanding Truthy and Falsy

# Python mein kuch values conditions mein True behave karti hain aur kuch False.

# Inhe Truthy aur Falsy values kehte hain.

# Common Falsy Values:
# - False
# - None
# - 0
# - 0.0
# - "" (empty string)
# - [ ] (empty list)
# - {} (empty dictionary)
# - set() (empty set)

# Inke alawa most values Truthy hoti hain.

# Example:

# username = ""

# if username:
#     print("Username provided")
# else:
#     print("Username is empty")


# Output:
# Username is empty


# Ab:

# username = "admin"

# if username:
#     print("Username provided")
# else:
#     print("Username is empty")


#     Output:
# Username provided


# Ye concept login systems, form validation aur user input checking mein useful hai.