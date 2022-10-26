"""

@Author: Ryan Eubanks
@Date: 10/25/2022

Problem Statement:
simulate a check-out counter

<Program> Welcome to the checkout counter! How many items are you purchasing today?
<User> 3 (user presses Enter key)
<Program> Please enter the name of product 1:
<User> chicken (user presses Enter key)
<Program> And how much does chicken cost?
<User> 3.50 (user presses Enter key)
<Program> Please enter the name of product 2:
<User> chips (user presses Enter key)
<Program> And how much does chips cost?
<User> 1.25 (user presses Enter key)
<Program> Please enter the name of product 3:
<User> gum (user presses Enter key)
<Program> And how much does gum cost?
<User> .99 (user presses Enter key)
<Program>
Your order was:
     chicken $3.50
     chips $1.25
     gum $.99

Your subtotal comes to $5.74. With 9% sales tax, your total is $6.26.
Please enter cash amount:
<User> 20.00 (user presses Enter key)
<Program>
I owe you back $13.74.
Thank you for shopping with us!
"""

def main():

    shopping_Cart = {}

    num_items = int(input("Welcome to the check out counter! How many items are you purchasing today? "))

    for i in range(1,num_items):
        product = input(f"Please enter the name of product {i} : ")
        price = float(input(f"And how much does {product} cost? "))

        shopping_Cart[product] = price

    print("Your order was: ")
    for key, values in shopping_Cart.items():
        print("%s \t"%(shopping_Cart.get()))
main()
