#Identify the Nature of a Number
a = int(input())
if a > 0:
  print("POSITIVE")
elif a < 0:
  print("NEGATIVE")
else:
  print("ZERO")

#Explore Math Functions
import math
a = float(input())
b = int(input())
c = int(input())
d = int(input())
print(math.floor(a))
print(math.ceil(a))
print(round(a))
print(int(math.sqrt(b)))
print(pow(c,d))

#Smallest of Four Numbers
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))

#Truncate to Two Decimal Places
import math
a = float(input())
print(math.trunc(a*100)/100)

#Find Second Maximum Number
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
  print("No second max")
elif a>=b and a>=c:
  print(max(b,c))
elif b>=a and b>=c:
  print(max(a,c))
else:
  print(max(a,b))


