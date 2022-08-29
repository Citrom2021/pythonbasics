#(basics)
print("Két user input szám bekérése majd átlag számítása")
num = 2
total_sum = 0
for n in range(num):
    numbers = float(input('Adja meg a dolgozata elért pontszámát  : '))
    total_sum += numbers
avg = total_sum/num
print(num,' db dolgozat átlaga:', avg)
print("Két szám átlagánál mindkét szám mindig ugyanannyira tér el az átlagtól")
