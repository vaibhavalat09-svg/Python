# number in a list and stop when found 
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter a number to search: "))

for num in numbers:
    if num == search:
        print("Number found:", num)
        break
else:
    print("Number not found.")