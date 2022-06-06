#python program to check if a number is Positive or Negative

num = input("Please type an integer: ") 
num = int(num) 

if num < 0: 
    result = "Negative" 
else: 
    result = "Positive" 

print("This number is: ", result)
