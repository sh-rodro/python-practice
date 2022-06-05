#python program to check leap year

year = input("Enter year: ") 
year = int(year) 

if year % 400 == 0: 
  result = "a leap year" 
elif year % 100 == 0: 
  result = "not a leap year" 
elif year % 4 == 0: 
  result = "a leap year" 
else: 
  result = "not a leap year" 
  
print("This year is: ", result)
