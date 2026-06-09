#=========================================Beginner===================================================

#========Q1 = Print numbers from 1-10 using a for loop====================#

for z in range(1,11):
    print(z)

#========Q2 = print all numbers from 1-20, each on a new line==================#

for z in range(1,21):
    print(z)

#==========Q3 = print the multiplication table of 5 (5 * 1-5 *10)==========================#

num = 5
for z in range(1, 11):
    print(str(num) + " x " + str(z) + " = " + str(num * z))

#=========Q4 = Calculate and print the sum of numbers 1-100=================================#

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

#=======Q5 = print all even numbers between 1 and 20===============================#

for z in range(2, 21, 2):
    print(z)

#==========================================Intermediate========================================#

#=========Q1 = Ask the user for a number and print it's multiplication table up to 10===============#


num = int(input("Enter a number: "))
for z in range(1, 11):
    print(str(num) + " x " + str(z) + " = " + str(num * z))

#=======Q2 = Count how many vowels (a, e, i, o, u) are there in a string===================#


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#===========Q3 = print the followwing pattern(*, **, ***, ****, *****)=========================#

for z in range(1, 6):   
    print("*" * z)

#==========================Q4 = Find the largest number in the follwing list:==========================#
#                          numbers = 12, 45, 2, 67, 34, 89, 23

numbers = [12, 45, 2, 67, 34, 89, 23]

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print(largest)

#============Q5 = Reverse a string using a for loop===========================#


text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

#========================================HARD===================================================

#=============Q1 = print the following inverted triangle pattern:=====================#
#                       *****
#                       ****
#                       ***
#                       **
#                       *

for z in range(5, 0, -1):   
    print("*" * z)

#=========Q2 = Create the following right-angled triangle pattren:===========================#
#              *
#             **
#            ***
#           ****
#          *****

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)