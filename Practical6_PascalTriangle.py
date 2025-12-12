# Write a python program to construct pascal's triangle for a given number of rows. Use for loop
# Output with rows: 5

'''
Pascal's Triangle Example (with 5 rows):
                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4       1
'''

rows = int(input("Please enter the number of rows: "))

for i in range(rows):
    for j in range(rows, i, -1):
        print("  ", end="")
    num = 1

    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)
    print("\n",end="")
