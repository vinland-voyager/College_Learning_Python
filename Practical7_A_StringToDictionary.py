'''
Practical 7: Data structures in python
A. Given a string, create a dictionary where the keys are the words and the values are the length of those words.
'''

exStr = input("Enter a string: ")
exDict = {}
for word in exStr.split():
    exDict[word] = len(word)

print(exDict)
