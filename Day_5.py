# # Operators in Python

# # Arithmetic · Comparison · Logical · Assignment · Identity · Membership · Bitwise

# 1. Operators kya hote hain?
# Operators special symbols ya keywords hote hain jo variables aur values par operations perform karte hain.

# Example:

# a = 10
# b = 5

# result = a + b

# print(result)

# Output:
# 15


# Is example mein:
# - a aur b = Operands
# - + = Operator
# - a + b = Expression
# - 15 = Result


# Python Operators ki 7 categories


# | Category | Operators |
# |---|---|
# | Arithmetic | + - * / // % ** |
# | Assignment | = += -= *= etc. |
# | Comparison | == != > < >= <= |
# | Logical | and or not |
# | Identity | is, is not |
# | Membership | in, not in |
# | Bitwise | &, |, ^, ~, <<, >> |


# 2. Arithmetic Operators

# Arithmetic operators mathematical calculations ke liye use hote hain.

# Operator	        Name	            Example	    Result

# +	                Addition	        10 + 5	    15
# -	                Subtraction	        10 - 5	    5
# *	                Multiplication	    10 * 5	    50
# /	                Division	        10 / 5	    2.0
# //	            Floor Division	    11 // 5	    2
# %	                Modulus	            11 % 5	    1
# **	            Exponentiation	    2 ** 3	    8

# 2.1 Addition, Subtraction, Multiplication

# a = 20
# b = 10

# print(a + b)  # Addition: 30
# print(a - b)  # Subtraction: 10
# print(a * b)  # Multiplication: 200

# # # 2.2 Division /

# print(10 / 2)
# print(10 / 3)

# Output:
# 5.0
# 3.3333333333333335

# Python ka / operator division ka result float mein deta hai.


# 2.3 Floor Division //
# Ye result ko neeche wale integer tak floor karta hai.

# Output:
# 5
# 5
# -6

# Dhyan do: Negative numbers mein floor division zero ki taraf truncate nahi karta, balki lower integer deta hai.


# 2.4 Modulus %
# Division ke baad remainder return karta hai.


# print(10 % 3)
# print(20 % 5)
# print(17 % 4)


# Output:
# 1
# 0
# 1


# Practical: Even / Odd Checker

# number = int(input("Enter Your number: "))
# if number % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# Yahan number % 2 remainder check karta hai.


# 2.5 Exponentiation **
# Power calculate karne ke liye:

# print(2 ** 3)
# print(5 ** 2)
# print(3 ** 4)

# Output:
# 8
# 25
# 81


# 2.6 Arithmetic ka combined example

# a = 20
# b = 6

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Power:", a ** b)



# 3. Comparison Operators

# Comparison operators do values ko compare karte hain aur result True ya False dete hain.

# Operator	    Meaning	                Example	        Result

# ==	        Equal to	            10 == 10	    True
# !=	        Not equal to	        10 != 5	        True
# >	            Greater than	        10 > 5	        True
# <	            Less than	            5 < 10	        True
# >=	        Greater than or equal	10 >= 10	    True
# <=	        Less than or equal	    5 <= 10	        True

# # Examples

# a = 10
# b = 20

# print(a == b)  # False
# print(a != b)  # True
# print(a > b)   # False
# print(a < b)   # True
# print(a >= 10) # True
# print(b <= 20) # True



# Important: = vs ==

# =	                        ==
# Assignment operator	    Comparison operator
# Value assign karta hai	Values compare karta hai
# age = 20	                age == 20


# 3.1 Chained Comparisons

# Python mein multiple comparisons ek hi expression mein likh sakte hain.


# age = 20
# print(18 <= age <= 60)


# # Output:
# # True


# # Iska matlab hai:

# 18 <= age and age <= 60



# Dono conditions True honi chahiye.
# Practical: Marks Checker


# marks = float(input("Enter Your Marks: "))
# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")


# 4. Logical Operators
# Logical operators multiple conditions ko combine karte hain.

# Python mein 3 logical operators hain:

# - and
# - or
# - not

# 4.1 AND Operator
# and tabhi True deta hai jab dono conditions True hon.

# age = 20
# is_has = True

# result = age >= 18 and is_has == True
# print(result)
    

# Output:
# True


# AND       Truth       Table

# A	        B	        A and B
# True	    True	    True
# True	    False	    False
# False	    True	    False
# False	    False	    False


# 4.2 OR Operator
# or tab True deta hai jab kam se kam ek condition True ho.


# has_email = True
# has_phone = False

# result = has_email or has_phone
# print(result)

# Output:
# True


# OR    Truth   Table
# A	    B	    A or B
# True	True	True
# True	False	True
# False	True	True
# False	False	False


# 4.3 NOT Operator
# not Boolean result ko reverse karta hai.

# is_blocked = False
# print(not is_blocked)

# Output:
# True


# NOT Truth Table

# A	        not A

# True	    False
# False	    True




# 4.4 Short-Circuit Evaluation

# Ye logical operators ka important advanced concept hai.

# Python and aur or mein kabhi-kabhi second condition ko evaluate hi nahi karta, kyunki first condition se result already decide ho jata hai.

# Example:


# x = 10
# result = x > 5 or x / 0 > 1
# print(result)

# Output:
# True


# Kyun error nahi aaya?
# - x > 5 True hai.
# - or mein ek condition True hone par result True ho jata hai.
# - Isliye Python ne x / 0 execute nahi kiya.

# Is behavior ko short-circuit evaluation kehte hain.


# 5. Assignment Operators
# Assignment operators variables ko values assign ya update karne ke liye use hote hain.

# Ye W3Schools ke operator groups ka ek important section hai. 
# W3Schools+1

# 5.1 Basic Assignment

# x = 10

# print(x)

# Output: 10



# 5.2 Compound Assignment Operators

# Operator	    Example	    Equivalent
# =	            x = 5	    x = 5
# +=	        x += 3	    x = x + 3
# -=	        x -= 3	    x = x - 3
# *=	        x *= 3	    x = x * 3
# /=	        x /= 3	    x = x / 3
# //=	        x //= 3	    x = x // 3
# %=	        x %= 3	    x = x % 3
# **=	        x **= 3	    x = x ** 3

# Example:


# score = 50

# score += 10
# print(score)

# score -= 5
# print(score)

# score *= 2
# print(score)


# Output:
# 60
# 55
# 110


# Step-by-step:

# 1. Initially score = 50
# 2. score += 10 → 60
# 3. score -= 5 → 55
# 4. score *= 2 → 110




# 5.3 Bitwise Assignment Operators

# Python mein bitwise operators ke assignment versions bhi hain:

# | Operator | Example |
# |---|---|
# | &= | x &= 3 |
# | |= | x |= 3 |
# | ^= | x ^= 3 |
# | >>= | x >>= 1 |
# | <<= | x <<= 1 |

# Inhe Bitwise section mein detail se samjhenge.



# 6. Identity Operators

# Identity operators check karte hain ki do variables same object ko refer karte hain ya nahi.

# Python mein do identity operators hain:
# - is
# - is not

# Yahan ek important difference samjho:
# - == values compare karta hai.
# - is object identity compare karta hai.

# Example

# list1 = [10, 20, 30]
# list2 = [10, 20, 30]
# list3 = list1

# print(list1 == list2)
# print(list1 is list2)
# print(list1 is list3)

# Output:
# True
# False
# True

# Kyun?
# - list1 aur list2 ki values same hain, lekin dono separate list objects hain.
# - list3 = list1 ke kaaran dono variables same list object ko refer karte hain.


# Visual understanding 

# list1                     # list2
# [10, 20, 30]              # [10, 20, 30]
# Object A                  # Object B


# Same values, different objects. 

# list1 is list3 → True
# Dono ek hi object ko refer karte hain.




# 'is None' ka use
# Python mein 'None' check karne ke liye 'is None' recommended hai.


# result = None

# if result is None:
#     print("No result available")


# Output:
# No result available


# None ko check karne ke liye == None ke bajaye is None use karo.




# 7. Membership Operators

# Membership operators check karte hain ki koi value kisi sequence ya collection ke andar present hai ya nahi.

# Do operators:
# - in
# - not in


# 7.1 'in' Operator

# languages = ["Python", "Java", "JavaScript"]

# print("Python" in languages)
# print("C++" in languages)

# # Output:
# True
# False


# 7.2 not in Operator

# languages = ["Python", "Java", "JavaScript"]

# print("Java" not in languages)
# print("C++" not in languages)

# Output:
# False
# True



# 7.3 String ke saath Membership

# email = "student@example.com"

# print("@" in email)
# print("gmail" in email)

# Output:
# True
# False



# Practical: Allowed User Checker

# allowed_users = ["admin", "vashu", "dsvv"]

# username = input("Enter your username: ")

# if username in allowed_users :
#     print("User found")
# else:
#     print("User not found")


# Cybersecurity connection: Membership operators allowlist checks mein useful ho sakte hain. Lekin actual authentication ke liye sirf username list check karna sufficient security nahi hai.



# 8. Bitwise Operators

# Important Advanced Concept
# Bitwise operators numbers ke binary bits par operations perform karte hain.

# Binary system mein sirf do digits hoti hain:
# - 0
# - 1
# Example:

# print(bin(5))
# print(bin(3))

# Output:
# 0b101
# 0b11



# 8.2 Bitwise OR (|)

# Koi bhi ek bit 1 ho toh output 1 hoti hai.
# print(5 | 3)


# Calculation:
#   0101
# | 0011
# ------
#   0111


# Output: 7


# 8.3 Bitwise XOR (^)

# Dono bits different hon toh 1, same hon toh 0.
# print(5 ^ 3)

# Calculation:
#   0101
# ^ 0011
# ------
#   0110


# Output: 6


# 8.4 Bitwise NOT (~)

# Bits ko invert karta hai. Python integers signed representation use karte hain, isliye:
# print(~5)

# Output:
# -6


# Python mein ~x ka result -(x + 1) hota hai.


# 8.5 Left Shift (<<)

# Bits ko left side shift karta hai.
# print(5 << 1)print(5 << 2)

# Output:
# 10
# 20


# Positive integers ke liye left shift by 1 ka effect 2 se multiply karne jaisa hota hai.

# 8.6 Right Shift (>>)

# Bits ko right side shift karta hai.
# print(8 >> 1)print(8 >> 2)

# Output:
# 4
# 2


# Positive integers ke liye right shift by 1 ka effect integer floor division by 2 jaisa hota hai.


# Bitwise Operators Summary

# | Operator | Name | Example | Result |
# |---|---|---|---:|
# | & | AND | 5 & 3 | 1 |
# | | | OR | 5 | 3 | 7 |
# | ^ | XOR | 5 ^ 3 | 6 |
# | ~ | NOT | ~5 | -6 |
# | << | Left Shift | 5 << 1 | 10 |
# | >> | Right Shift | 8 >> 1 | 4 |

# Cybersecurity connection: Bitwise operations permissions, binary flags, protocol fields aur low-level data processing mein kaam aate hain. Lekin bitwise operations ko encryption ka replacement nahi samajhna chahiye.



# 9. Conditional Expression (Ternary Operator)

# Python mein ek short way hai condition ke basis par value choose karne ka.

# Syntax:

# value_if_true if condition else value_if_false

# Example:

# age = 20

# status = "Adult" if age >= 18 else "Minor"

# print(status)


# Output:
# Adult


# Same program normal if-else mein:


# age = 20

# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# print(status)


# Dono ka result same hai.



# 10. Operator Precedence

# Jab ek expression mein multiple operators hote hain, Python ek particular order follow karta hai.

# Isko Operator Precedence kehte hain. W3Schools aur Python documentation dono is order ko explain karte hain.


# Example :

# result = 10 + 5 * 2

# print(result)

# Output:
# 20

# Kyun?
# 1. Multiplication pehle: 5 * 2 = 10
# 2. Addition baad mein: 10 + 10 = 20


# Precedence Table
# Highest priority se lowest priority tak.

# | Priority | Operators |
# |---:|---|
# | 1 | () |
# | 2 | ** |
# | 3 | +x, -x, ~x |
# | 4 | *, /, //, % |
# | 5 | +, - |
# | 6 | <<, >> |
# | 7 | & |
# | 8 | ^ |
# | 9 | | |
# | 10 | Comparisons, is, in |
# | 11 | not |
# | 12 | and |
# | 13 | or |




# Practice

# print(2 + 3 * 4)
# print((2 + 3) * 4)
# print(10 > 5 and 20 < 30)
# print(not True or False)


# Output:
# 14
# 20
# True
# False

#  Pro tip: Jab expression complex ho, parentheses use karo. Code readable aur understandable rahega.