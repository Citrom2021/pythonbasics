#(Python testing)
print("Just a basic python")
num1 = float(input("Add first number: "))
num2 = float(input("Add second number: "))
num3 = float(input("Add third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The biggest number is:",largest)
