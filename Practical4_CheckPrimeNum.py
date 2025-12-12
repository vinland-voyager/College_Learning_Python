'''
Practical 4:
Write a python program to check given number is a prime number or not
Use while loop and if-else
Show factors that are not prime
'''

num = int(input("Enter the number to be checked: "))
counter = 2
count = 0

while counter < num:
    if num % counter == 0:
        count += 1
        print(f"{num} is divisible by {counter}")
    counter += 1

if num > 1:
    if count > 0:
        print(f"{num} is NOT a Prime Number.")
    else:
        print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")

