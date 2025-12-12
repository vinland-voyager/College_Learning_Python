'''
Practical 7: Data structures in python
C. Rotate elements in a tuple by 'n' positions to the left and right
'''

inList = []
while True:
    num = input("Please enter a number or press enter to proceed: ")
    if not num:
        break
    inList.append(int(num))

tupleX = tuple(inList)

change = int(input("\nEnter the change: \n"))
change = change % len(tupleX)
tupleX_left = tupleX[change:] + tupleX[:change]
tupleX_right = tupleX[-change:] + tupleX[:-change]

print(f"Original Tuple: {tupleX}")
print(f"Left-Shift Tuple: {tupleX_left}")
print(f"Right-Shift Tuple: {tupleX_right}")
