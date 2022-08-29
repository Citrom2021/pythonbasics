a = 75 * 25
b = 75 * 25
c = (75 * 25) / 2
gy= 1
# totalgy = ?

tegla1= a
print ("\nElső téglalap területe: %20.2f m2" % tegla1)

tegla2= b
print ("Második téglalap területe: %17.2f m2" % tegla2)

négyzet = c
print ("A négyzet területe: %23.2f m2" % négyzet)

terulettotal = a+b+c
print("Gyeptéglával fedésre váró terület: %9.2f m2" % terulettotal)
print("Szükséges gyeptégla: %23.2f db" % terulettotal)


from time import sleep
count = 0.5
while count <= a +b +c:
    print("Szükséges mennyiség ellenőrzése:%12.2f" % count,"db", end="\r")
    sleep(0.0)
    count += 0.5



