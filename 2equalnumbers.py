#Program to check if user input are equal without using any comparison opertor.

def checkIfSame(number1, number2):

#user XOR operator as a^a is always 0
 if ((number1 ^ number2) !=0):
   print("Numbers are not equal")
 else:
   print("Both numbers are equal")

#Taking input
number1 = int(input("Enter first number to comapare:"))
number2 = int(input("Enter second number to compare :"))

checkIfSame(number1, number2)
