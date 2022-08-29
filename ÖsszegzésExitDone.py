negyvenkilencfölött = None
negyvenkilencalatt = None
while True:
    num = input("Írjon számot vagy 'done': ")
    try:
        if num == "done":
          break
        num = float(num)
    except:
        print ("Kérem számot üssön vagy 'done'")
        continue
    if negyvenkilencalatt is None or negyvenkilencfölött is None:
        negyvenkilencalatt = num
        negyvenkilencfölött = num
    elif num < 50:
        print ("49-nél vagy nagyobb számot üssön!")
    elif negyvenkilencfölött > 49:
        negyvenkilencfölött += num
print ("A számok összege", negyvenkilencfölött)

