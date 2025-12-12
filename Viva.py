def viewCart():
    print("\n| Product\t\t\t | Quantity\n------------------------------------------")
    for product in shoppingCart:
        print(f" | {product}\t | {shoppingCart[product]}")

def addItem(product, quantity):
    if product not in productDict.keys():
        print("Product not in the catalogue.")
        return 1
    if product not in shoppingCart.keys():
        shoppingCart[product] = quantity
    else:
        shoppingCart[product] += quantity

def billing(cart, index=0):
    if index == len(cart):
        return 0
    subtotal = cart[index][1] * cart[index][2]
    return subtotal + billing(cart, index + 1)

productDict = {"Rice":100, "Wheat Flour":40}
shoppingCart = {}
while True:
    option = int(input("\n1. Add item\n2. View Cart\n3. Billing\n4. Exit\n"))
    if option == 1:
        print("| Product\t\t\t | Price----------------------------------------\n")
        for item in productDict:
            print(f" | {item}\t | {productDict[item]}")
        item = input("\nSelect an option from the list: ")
        qty = int(input("\nEnter Quantity: "))
        addItem(item.capitalize(), qty)

    elif option == 2:
        viewCart()

    elif option == 3:
        if not shoppingCart:
            print("Cart empty.")
        else:
            lst = [(product, productDict[product], quantity) for product, quanitty in shoppingCart.items()]
            bill = billing(lst)

    elif option == 4:
        break