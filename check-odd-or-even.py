#python program to check if a number is Odd or Even

num = input("Enter an integer: ") 
num = int(num) 

if num % 2 == 0: 
  result = "Even" 
else: 
  result = "Odd"

print("This number is: ", result)
