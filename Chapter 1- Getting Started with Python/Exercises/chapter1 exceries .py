# Exercise 1: Print Strings :ballot_box_with_check:
#Write a Python program to print the following string in a specific format.
#Twinkle, twinkle, little star,
	#How I wonder what you are! 
		#Up above the world so high,   		
		#Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
	#How I wonder what you are
# This is the solution of exercise
print("Twinkle, twinkle, little star,")
print("    How I wonder what you are!")
print("        Up above the world so high,")
print("        Like a diamond in the sky. ")
print("Twinkle, twinkle, little star,")
print("    How I wonder what you are")

# Exercise 2: Print the Version of Python :ballot_box_with_check:
#Write a Python program to get the Python version you are using.
#This is the solution of exercise
import sys
print("python version")
print (sys.version)

# Exercise 3: Print date and Time :ballot_box_with_check:
#Write a Python program to display the current date and time.
#This is the solution of exercise
import datetime 
current_datetime = datetime.datetime.now()
print("The current date and time is ",current_datetime)

# Exercise 4: Strings Concatination :ballot_box_with_check:
#Write three strings in different variables and print the output as one string.
#This is the solution of exercise
A="I"
B="miss"
C="you"
print(A," "+ B," "+ C)

# Exercise 5: Compute area of Circle :ballot_box_with_check:
#Write a Python program which accepts the radius of a circle from the user and compute the
PI=3.14
r=float(input("Enter the radius "))
area=PI*r*r
print("the erea of a circal is",area)










