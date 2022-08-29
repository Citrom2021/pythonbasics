"""
sum = 0
number = 1
while number > 0:
    number = int(input('Enter a positive number: '))
    if number > 0:
        sum = sum + number
print("The sum of the numbers is", sum)
"""
from datetime import date
today = date.today()
d1 = today.strftime("%d %B %Y")
print("AT Welsch, " , d1)

sum = 0
number = 1
while True:
	print("\nNegatív számmal bejezheti a programot")
	number = int(input("Adjon meg egy számot nulla felett: "))
	if number >49:
		sum += number
	if  50 > number >0:
		print("Adjon számot 49 felett!")
	if number < 0:
		break

print("A számok összege", sum)
