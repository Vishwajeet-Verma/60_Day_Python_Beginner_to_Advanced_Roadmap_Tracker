# # PART 1 – Introduction to Python
# # 1. What is Python?
# # Python is a high-level, interpreted, general-purpose programming language.

# # Simple language mein:

# # Python ek programming language hai jiska use hum computer ko instructions dene ke liye karte hain.

# # For example, agar tum computer se kehna chahte ho:
# # - Do numbers ko add karo.
# # - Kisi user ka password check karo.
# # - Website create karo.
# # - Files ko read karo.
# # - Network scan karo.
# # - Cybersecurity tools develop karo.
# # Toh hum Python code likhkar computer ko ye instructions de sakte hain.


# # Example:
# # print("Hello, World!")



# # Output:
# # Hello, World!


# # Yahan print() Python ka built-in function hai jo screen par output display karta hai.



# # 2. History of Python



# Creator: Guido van Rossum
# - Python development started: 1989
# - First public release: 1991
# - Python 2.0: 2000
# - Python 3.0: 2008
# - Current major generation: Python 3


# Python ka naam snake se nahi, balki British comedy show Monty Python's Flying Circus se inspired hai.






# 3. Why is Python so popular?

# Python popular hone ke kuch important reasons hain:

# Feature	                Explanation

# Easy to Learn	            Simple syntax
# Open Source	            Free to use
# Interpreted	            Code interpreter ke through execute hota hai
# Cross Platform	        Windows, Linux, macOS
# Huge Libraries	        Ready-made modules available
# Community Support	        Large developer community
# Versatile	                Multiple fields mein use






# 4. Where is Python used?


# Cybersecurity

# Network scanning, log analysis, automation, security testing.



# AI & Machine Learning

# Predictive models, automation and intelligent applications.



# Web Development

# Backend development using Django, Flask and FastAPI.



# Data Science

# Data analysis, visualization and processing.



# Automation

# Repetitive tasks, file management and system administration.








# PART 2 – How Python Works

# 5. How does Python execute code?
# Jab tum Python code likhte ho, toh Python implementation us code ko execute karne ke liye internally multiple steps perform karti hai.

# Simplified CPython execution process:


# 1. Python Source Code

# hello.py

#     ↓

# 2. Parser / Compiler

# Code is compiled into bytecode

#     ↓

# 3. Python Bytecode

# Intermediate instructions

#     ↓

# 4. Python Virtual Machine (PVM)

# Executes bytecode

#     ↓

# Final Output


# Important: Python ko commonly interpreted language kaha jata hai, lekin CPython internally bytecode compilation bhi karta hai. Isliye ye kehna ki Python directly source code ko line-by-line execute karta hai, technically incomplete explanation hai.



# 6. Compiler vs Interpreter


# Compiler	Interpreter
# Usually translates code before execution	Executes program through an execution environment
# Compilation step produces executable or intermediate code	Execution often happens through runtime instructions
# Example: C compiler	Example: Python runtime

# Python mein CPython compiler aur interpreter dono ka role hota hai.









# PART 3 – Python Installation


# 7. Install Python on Windows 11


# Step 1: Official website open karo:

# Download Python – Official WebsiteStep 2: Latest stable Python 3 version download karo.

# Step 3: Installer open karo.

# Step 4: Installation ke time:
# - Add python.exe to PATH checkbox select karo.
# - Click Install Now.
# - Installation complete hone do.

# Step 5: Verify installation.

# # Windows Command Prompt (CMD) open karo aur likho:

# python --version


# Expected output (version number tumhare installation ke according hoga):
# Python 3.x.x


# Agar python command work nahi karti, toh ye try karo:
# py --version


# 8. Understand Python PATH

# PATH ek environment variable hai jo operating system ko batata hai ki executable programs ko kin directories mein search karna hai.

# Example:

# Jab tum CMD mein likhte ho:
# python


# Windows PATH mein Python executable ko locate karne ki koshish karta hai.

# Isliye installation ke time Add Python to PATH important hai.






# PART 4 – IDE and Code Editor


# 9. What is an IDE?

# IDE stands for Integrated Development Environment.

# IDE ek software hota hai jisme developers code write, run, test aur debug kar sakte hain.

# Popular Python development tools:

# Visual Studio Code

# Lightweight code editor with extensions and debugging support.

# PyCharm

# Dedicated Python development IDE.


# Jupyter Notebook

# Interactive coding environment, popular for data science.



# VS Code setup for Python

# 1. Install Visual Studio Code.
# 2. Open VS Code.
# 3. Open Extensions (Ctrl + Shift + X).
# 4. Search Python.
# 5. Install the official Microsoft Python extension.
# 6. Create a folder named Python-60-Days.
# 7. Create a file named day01.py.






# PART 5 – Your First Python Program



# 10. Hello World

# Ab hum apna first Python program likhenge.

# File name:

# day1.py


# print("Hello, World!")
# print("My name is Hlo.")
# print("I am learning Python.")
# print("This is Day 1 of my 60-Day Roadmap.")


# Output:

# Hello, World!
# My name is Hlo.
# I am learning Python.
# This is Day 01 of my 60-Day Roadmap.



# Understanding print()

# print() Python ka built-in function hai.

# Iska use output display karne ke liye hota hai.

# print("Python")
# print(100)
# print(10 + 20)


# Output:

# Python
# 100
# 30


# Notice karo ki 10 + 20 ka result 30 aaya, kyunki Python ne mathematical addition perform kiya.



# 11. Understanding Python Syntax

# Syntax ka matlab hota hai programming language ke rules.

# Python mein kuch basic syntax rules:


# Rule 1 – Case Sensitivity
# name = "Vishwajeet"
# 
# print(name)


# Python mein name aur Name alag variables hain.



# Rule 2 – Indentation

# Python code blocks ko define karne ke liye indentation use karta hai.
# if 10 > 5:    
#     print("10 is greater")


# Yahan print() ke aage 4 spaces hain.




# Rule 3 – Comments

# Comments ka use code explain karne ke liye hota hai.


# # This is my first Python comment
# print("Learning Python")



# Python # ke baad wali line ko comment ke roop mein treat karta hai.


# Rule 4 – Multiple Statements

# print("Hello")
# print("Welcome")
# print("Python")


# Har statement alag line par execute hota hai.





# 12. Python Interactive Mode vs Script Mode

# Python mein code execute karne ke do common methods hain.

# Interactive Mode	                Script Mode

# Commands directly execute	        Code saved in .py file
# Useful for quick testing	        Useful for complete programs
# Uses Python shell	                Uses Python file

# Interactive mode start karo:

# python

# Then:
# >>> 10 + 2030

# Exit karne ke liye:
# exit()


# Script mode:
# python day01.py

# Ye tumhari file execute karega.





# PART 6 – Common Errors

# Programming seekhte time errors aana normal hai.

# Aaj ke liye ye 4 errors samajhna important hai.

# 1. SyntaxError
# print("Hello"

# Closing bracket missing hai.


# 2. NameError
# print(username)

# Agar username define nahi hai, toh NameError aayega.


# 3. IndentationError
# if 10 > 5:
# print("Hello")

# Yahan indentation missing hai.


# 4. TypeError
# print("Age: " + 20)

# String aur integer ko directly concatenate nahi kar sakte.

# Correct version:
# print("Age: " + str(20))





# PART 7 – Practical Assignments

# Ab sirf padhna nahi hai. Tumhe khud coding karni hai.

# Today's Practical Tasks

# Task 1 – Personal Introduction Program
# Ek Python program banao jo tumhari basic information display kare.

# Expected output:
# ================================
#        PERSONAL PROFILE
# ================================

# Name: Hello World
# Course: BCA
# Semester: 1st
# College: DSVV
# Goal: Cybersecurity 

# ================================



# Task 2 – Simple Calculator

# Program banao jo 2 numbers ka addition, subtraction, multiplication aur division display kare.

# Example:
# print("Addition:", 10 + 5)
# print("Subtraction:", 10 - 5)
# print("Multiplication:", 10 * 5)
# print("Division:", 10 / 5)




# Task 3 – Cybersecurity Introduction
# Ek program banao jo cybersecurity-related information display kare.

# Example:
# print("Cybersecurity Learning Journey")
# print("Python for Security Automation")
# print("Network Security")
# print("Ethical Hacking")
# print("System Security")




# Task 4 – Error Practice

# Khud se ye 3 errors generate karo aur unhe fix karo:
# - SyntaxError
# - NameError
# - IndentationError



# What you should remember today

# Aaj ke important concepts:
# 1. Python ek high-level, general-purpose programming language hai.
# 2. Python ke creator Guido van Rossum hain.
# 3. Python source files .py extension use karti hain.
# 4. print() output display karta hai.
# 5. Python indentation use karta hai.
# 6. VS Code ek code editor hai.
# 7. Python ko CMD se execute kar sakte hain.
# 8. Errors debugging aur learning ka important part hain.