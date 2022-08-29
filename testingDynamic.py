a = 75
b = 25
c = 12.5
d = 32.5

result = (float(a) * float(b))*2
result2 = float(c) * float(d)
result3 = result + result2
print (result3)

from sys import stdout
from time import sleep
for i in range(1,46876):
    stdout.write("\r%d" % i)
    stdout.flush()
    sleep(0.000000000001)
stdout.write("\n")

import sys
to = 20
digits = len(str(to - 1))
delete = "\b" * (digits)
for i in range(to):
   print("{0}{1:{2}}".format(delete, i, digits), end="")
   sys.stdout.flush()
   
