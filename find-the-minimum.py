#python program to the minimum of three numbers

num1 = input("Enter the first number: ") 
num2 = input("Enter the second number: ") 
num3 = input("Enter the third number: ") 

num1 = int(num1) 
num2 = int(num2) 
num3 = int(num3) 

if num1 < num2: 
    min = num1 
else: 
    min = num2 
if num3 < min: 
    min = num3 

result = min 

print("Minimum : ", result)
