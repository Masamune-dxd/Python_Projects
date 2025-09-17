### 1 ###

# print("Hello, World!")

# message = "Hello, World!"
# print(message)

# hello = "Hello,"
# world = "World!"
# print(hello + " " + world)

# name = input("Name: ")
# print(f"Hello, {name}")

# print("Hello,","World!")

# print("Hello,", end = " ")
# print("World!")

# print("Hello,", end="World")
# print("!")

# print("Hello", "Hello,", sep="-", end=" ")
# print("World!")

# print("Hello" * 2)

### 2 ###
#--------------------------------------------------------------------
# var = 1 
# print(var)
# var = var + 1 # var += 1
# print(var)
#--------------------------------------------------------------------
# # rectangle using replication 
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end = "")
# print("+" + 10 * "-" + "+")
#--------------------------------------------------------------------
# x = input("Enter a number: ") # The user enters 2
# print(type(x)) # print the variable TYPE 

### 3 ###
#--------------------------------------------------------------------
# age = int(input("Your age: "))
# vote = 18
# if age > vote:
#     print("Good")
# else:
#     print("no")
#--------------------------------------------------------------------
# age = int(input("Enter age: "))
# vote = 18
# if age == 0:
#     print("No good")
# elif age < 18:
#     print("Not old enough")
# else:
#     print("Good enough") 
#--------------------------------------------------------------------
# number = int(input("Enter no.: "))
# while number != 0:
#     if number % 2 == 0:
#         print("Even")
#     else: 
#         print("Odd")
#     number = int(input("Enter no.: "))
#--------------------------------------------------------------------
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

#--------------------------------------------------------------------
# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# guess = int(input("Enter number: "))

# while guess != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     guess = int(input("Enter number again: "))

# print("Well done, muggle! You are free now.")
#--------------------------------------------------------------------
# for i in range(10):
#     print("The value of i is currently", i)
#--------------------------------------------------------------------
# for i in range(2, 8):
#     print("The value of i is currently", i)
#--------------------------------------------------------------------
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

#--------------------------------------------------------------------
# import time 

# countdown = 1
# for countdown in range(1, 6):
#     print(countdown, "Mississippi")
#     countdown += 1

# print("Ready or not, here I come")

#--------------------------------------------------------------------
# break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")

#--------------------------------------------------------------------
# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
#--------------------------------------------------------------------
# user_word = input("Enter a word: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
#     print(letter)
#--------------------------------------------------------------------
# word_without_vowels = ""

# user_word = input("Enter a word: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
#     word_without_vowels += letter

# print(word_without_vowels)
#--------------------------------------------------------------------
