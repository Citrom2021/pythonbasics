
a = 75
b = 25
gyeptegla = 1 * 1

nagyTerulet = (a * b) * 2
print("Nagy Terület: %29.2f m2" % nagyTerulet)

kisTerulet = (nagyTerulet / 2) / 2
print("Kis Terület: %30.2f m2" % kisTerulet)

print("egy db gyeptegla területe:%17.0f m2" % gyeptegla)

total = nagyTerulet + kisTerulet

szuksegesGyepMennyiseg = (nagyTerulet + kisTerulet) / gyeptegla

print("Össz fedni való terület: %18.2f m2" % total)

print("Szükséges gyeptégla mennyiség: %12.2f db" % szuksegesGyepMennyiseg)
