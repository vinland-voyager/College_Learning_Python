'''
Practical 7: Data structures in python
B. Given a list of Integers , find all pairs whose sum is equal to a given target
'''

numList = []
targetList = []

while True:
    num = input("Please enter a number or leave blank to proceed: ")
    if not num:
        break
    numList.append(int(num))

target = int(input("\nEnter the target number: "))

for num in numList:
    for numY in numList:
        if num + numY == target:
            targetList.append([num, numY])

for element in targetList:
    for elementY in targetList:
        if element == elementY or element.reverse() == elementY:
            targetList.remove(elementY)

print(f"\nTarget List: {targetList}")
