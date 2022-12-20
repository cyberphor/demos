
# How to Learn Any New Skill
# 1. learn the basics
# 2. learn how to break it (the boundaries, limitations, what doesn't work)
# 3. teach it (tell people what you learned to do and not do)

# Semantics: what things mean
# Syntax: where things go

# CRLF (Carriage Return, Line Feed)
# - New line: \n
# - Return: \r

# TTY (Teletype), VTY (Virtual Teletype)
# - Another carry-on from old computer technology

# PEP 8
# Python Style Guide (most languages have a guide on how to write in it)
# - ex: number of spaces, comments, etc. 

# OTBS
# One True Brace Style

# chapter 1: output
# - lesson 1: output to the console
# - lesson 2: output to a file
# - lesson 3: output to the network
"""
print("Hello world!")
print("Good morning!")
"""

# chapter 2: input
# - lesson 1: from the console
# - lesson 2: from a file
# - lesson 3: from the network
"""
name = input("What is your name? ")
print(name)
"""

# chapter 3: operators (arithmetic/math)
# - lesson 1: add strings, integers, etc. 
# - lesson 2: subtract etc. 
# - lesson 3: add, slice from an array/list, etc. 
"""
name = input("What is your name? ")
print("Hello " + name)
"""

# chapter 4: conditionals
# - lesson 1: if/else statement
# - lesson 2: elif statement
# - lesson 3: switch/case statement
"""
name = input("What is your name? ")
if (name == "Vic"): # name (IS EQUAL) vic; 
    message = "Hello " + "Chief" # message (IS) hello
else:
    message = "Hello " + name
print(message)
"""

# chapter 5: loops
# - lesson 1: for
# - lesson 2: while
# - lesson 3: until (not supported by all languages)
"""
names = "Batman", "Superman", "Wonder Woman"
for name in names:
  message = "Hello " + name
  print(message)
"""

# chapter 6: conditions
"""
def say_hello_to_stranger(name):
    message = "Hello " + name
    print(message)

def say_hello_to_friend(name):
    message = "Hello my friend, " + name
    print(message)

def main():
    person = input("What is your name? ")
    names = "Batman", "Superman", "Wonder Woman", person
    for name in names:
        if name == "Vic":
            say_hello_to_friend(name)
        else:
            say_hello_to_stranger(name)

main()
"""
