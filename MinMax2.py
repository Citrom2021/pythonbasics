largest = None
smallest = None
while True:
    num = input("Enter a number or type done: ")
    try:
        if num == "done":
            break
        num = float(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None or largest is None:
        smallest = num
        largest = num
    elif num < smallest:
        smallest = num
    elif num > largest:
        largest = num
print ("Maximum is", largest)
print ("Minimum is", smallest)
"""
largest = None
smallest = None
while True:
    num = input("Enter a number or type zero to print min & max: ")
    try:
        if num == "0":
            break
        num = float(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None or largest is None:
        smallest = num
        largest = num
    elif num < smallest:
        smallest = num
    elif num > largest:
        largest = num
print ("Maximum is", largest)
print ("Minimum is", smallest)

"""
