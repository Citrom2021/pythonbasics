number=None
less = 1
biggest = 1

while number != 0 :
	number = int(input("szám: ")) #0-val ki tudok szállni
	if(number < less):
		if number != 0:
			less = number
	if(number > biggest):
		if number != 0:
			biggest = number

print("Minimum: ", less, "Maximum: ", biggest)
