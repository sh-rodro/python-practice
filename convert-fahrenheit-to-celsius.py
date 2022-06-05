#python program to convert fahrenheit to celsius

f = input("Enter the temperature in fahrenheit: ") 
f = float(f) 

c = (f - 32) / 1.8 
c = round(c, 2) 

print("Temperature in celsius is: ", c)
