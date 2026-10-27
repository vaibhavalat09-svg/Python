# greater of two numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The greater number is:", a)
elif b > a:
    print("The greater number is:", b)
else:
    print("Both numbers are equal.")