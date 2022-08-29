b = int(input("Szam: "))
if (b<0) and (b % 2 == 0) :
	print("Negatív és párros")
elif (b < 0) and not( b % 2 == 0):
	print("Negatív és páratlan")
elif( b >0) and (b % 2 == 0):
	print("Pozitív és páros")
elif (b>0) and not(b %2 == 0):
	print("Pozitív és páratlan")
else:
	print("Pont nulla")

