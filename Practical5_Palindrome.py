'''
Practical 5:
Write a Python program to check whether a given number is a palindrome or not.
'''

number = int(input("Enter a number: "))
numlst = list(str(number))

if numlst == numlst[::-1]:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")
