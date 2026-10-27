# count the digits in a number 
num = int(input("Enter a number: "))
count = 0

num = abs(num)

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10

print("Number of digits:", count)