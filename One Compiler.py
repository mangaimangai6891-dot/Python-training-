#Input and Output Practice
a=int(input())
b=float(input())
c=str(input())
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)

#Progressive Float Execution
import struct
a = float(input())
a = struct.unpack('f', struct.pack('f',a))[0]
print("%.5f" % a)
print("%.4f" % a)
print("%.3f" % a)
print("%.2f" % a)
print("%.1f" % a)
print("%.0f" % a)

#Problem: Sum, Difference, Product, Division and Modulo
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  mod=abs(a)%abs(b)
  print(-1*mod)
else:
  print(a%b)

#ASCII
a=int(input())
print(chr(a))

#Update Counter
a=int(input())
a=a+5
a=a*2
a=a-3
print(a)

#ODD or EVEN
n = int(input())
print("Even" if n % 2 == 0 else "Odd")

#Greatest Among Three Numbers
a = int(input())
b = int(input())
c = int(input())
greatest = a if a > b and a > c else (b if b > c else c)
print(greatest)

#Character Digit to Integer
ch = input().strip().strip("'").strip('"')
print(int(ch))

#Personalized Greeting
name = input()
print(f"Hi {name}, welcome to the programming class!")

#Calculate Total and Average Marks
name = input()
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
total = a + b + c + d + e
average = total / 5
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks: {:.2f}".format(average))

#Shape Area Calculation
a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())
Square=a*a
rectangle=l*b
circle=3.14*r*r
triangle=(1/2)*B*h
print(f"Area of Square={Square}")
print(f"Area of Rectangle={rectangle}")
print(f"Area of Circle={circle:.2f}")
print(f"Area of Triangle={triangle:.0f}")

#Shape Perimeter Calculation Program
a = int(input())
b = int(input())
c = int(input())
d = int(input())
base1 = int(input())
side = int(input())
base2 = int(input())
square = 4 * a
rectangle = 2 * (b + c)
circle = 2 * 3.14 * d
triangle = base1 + side + base2
print(square)
print(rectangle)
print(f"{circle:.2f}")
print(triangle)

#Handling Mixed Inputs
a = int(input())
sentence = input()
print(a)
print(sentence)
