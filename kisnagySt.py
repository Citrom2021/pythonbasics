largest =float("-inf") # negative infinity
smallest = float("inf") # infinity
while True:
    inp = input("Enter a number, hit 0 and will show min & max: ")
    if inp == "0" : 
        break
    try:
        num = float(inp)
        largest = max(largest, num)
        smallest = min(smallest, num)
    except:
        print ("Invalid input")
        continue

print ("Maximum is ", largest)
print ("Minimum is ", smallest)
