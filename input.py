# input() = A function that allows user input OR 
#           A way to prompt for a value in your program OR
#           A function that prompt user to enter data
#          It returns the data entered as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: ")) # typecasting the input to integer

# age = age + 1 

# print(f"Hello {name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old.")

# Exercise 1 Rectangle Area Calculator
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))

# area = length * width
# print(f"The area of the rectangle is: {area}cm²") #Windows alt + 0178 for squared symbol  

# Exercise 2 Shopping Cart
item = input("Enter the item you want to buy: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?:"))

total = price * quantity
print(f"you have bought {quantity} x {item}/s")
print(f"Your total is: {total}FCFA")