listX = [1, 2, 3]
dictX = {"Name" : "Aayush", "Age" : 21}

try:
    num = int(input("Enter a number: "))
    index = int(input("Enter the index to check: "))
    print(listX[index])
    testX = input("Enter the key to check: ")
    testX = testX.capitalize()
    print(dictX[testX])
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    print(numerator / denominator)
    f = open("file.txt", "w")
    addition = num + f # to demonstrate TypeError
    import testinggg as gg

except ValueError:
    print("Value entered is not an integer.")
except IndexError:
    print("Index invalid.")
except KeyError:
    print("Key not found.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except FileNotFoundError:
    print("File not found.")
except ImportError:
    print("Module not found and therefore cannot be imported.")
except TypeError:
    print("Invalid data type.")
except:
    print("Something went wrong.")
finally:
    print("End of program.")