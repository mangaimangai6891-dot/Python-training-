# Triangle Angle Validation
a=int(input())
b=int(input())
c=int(input())
if a + b + c == 180 and a> 0 and b > 0 and c > 0:
  print("VALID")
  if a == b == c:
    print("EQUILATERAL")
  elif a == b or b == c or a == c:
    print("ISOSCELES")
  else:
    print("SCALENE")
else:
  print("NOT VALID")

#Number to Word
n = int(input())
words = ["zero","one","two","three","four",
          "five","six","seven","eight","nine"]
print(words[n])

#Vowel or Consonant
ch = input().lower()
if ch in "aeiou":
  print("vowel")
else:
  print("consonant")

#Leap Year Checker
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print("yes")
else:
  print("no")

#Fun Grade Calculator
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a + b + c + d + e) / 5
if avg >= 90:
  print("Excellent!")
elif avg >= 80:
  print("Great Job!")
elif avg >= 70:
  print("Good Effort!")
elif avg >= 50:
  print( "Keep Trying!")
else:
  print("Better Luck Next Time!")

#Train Berth Type Finder
seat = int(input())
no = seat%8
match no:
  case 1:
    print("LB")
  case 2:
    print("MB")
  case 3:
    print("UB")
  case 4:
    print("LB")
  case 5:
    print("MB")
  case 6:
    print("UB")
  case 7:
    print("SL")
  case 0:
    print("SU")

#Electricity Bill Calculator
units = float(input())
amount = 0.0
if units >= 0 and units <= 50:
  amount = units*1
elif units >= 51 and units <= 150:
  amount = 50 + (units-50)*2
elif units >= 151 and units <= 250:
  amount = 50 + 200 + (units-150)*3
else:
  amount = 50 + 200 + 300 + (units-250)*4
if amount >= 150:
  print(int(amount*0.2+amount))
else:
  print(int(amount))

#Thala vs Thalapathy Game
n=int(input())
if n%3 == 0 and n%5 == 0:
  print("ThalaThalapathy")
elif n%3 == 0:
  print("Thala")
elif n%5 == 0:
  print("Thalapathy")
else:
  print(n)

#Train Fare Calculator
age = int(input())
distance = int(input())
fare = distance * 5
if age < 12:
  fare = fare * 0.5
elif age <= 59:
  fare = fare
else:
  fare = fare * 0.75
print(int(fare)if fare.is_integer() else fare)

#Average Marks Calculator
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=a+b+c+d+e
avg=total/5
if avg.is_integer():
  print(int(avg))
else:
  print(f"{avg:.2f}")

#Fun Character Case Converter
a=input()
if a.islower():
  print(a.upper())
elif a.isupper():
  print(a.lower())
else:
  print("abcd theriyatha?")
  
