#Írjon programot, amely bekér számokat 0 végjelig, majd kiírja a legkisebbet és a legnagyobbat.
#Mentés: kisnagyn

number=None
less = 100
biggest = 1

while number != 0 :
	number = int(input("szám: ")) #0-val ki tudok szállni
	if(number < less):
		if number != 0:
			less = number
	elif(number > biggest):
		if number != 0:
			biggest = number

print("Minimum: ", less, "Maximum: ", biggest)
