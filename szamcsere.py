print("@Adam Welsch, Külker Gimi,Szoftver Esti,2020.09.29")
print("a és b érték vizsgálata, ha az a érték nagyobb, akkor számcsere")

a = int(input("Adja meg számban az a értéket: "))
b = int(input("Adja meg számban b értéket: "))
print("a érték: %.0f" % a)
print("b érték: %.0f" % b)

if ( a > b ) :
	a, b = b, a
	print("Az a érték a csere után: %.0f" % a)
	print("A b érték a csere után: %.0f" % b)
	
else:
	 print("Nincs szükség cserére")
