#Length of a string
s=input()
print(len(s))

#Join the strings
s1=input()
s2=input()
print(s1+" "+s2)

#Compare the Strings
s1=input()
s2=input()
if s1==s2:
  print("true")
else:
  print("false")

#First character of a string
n=input()
print(n[0])

#Last character of a string
n=input()
print(n[-1])

#Join first & last characters of a string
n=input()
print(n[0]+n[-1])

#Alphanumeric strings
s=input()
numcount=alphacount=False
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isdigit():
    numcount=True
if alphacount and numcount:
  print("true")
else:
  print("false")

#Uppercase check
s=input()
if s.isupper():
  print("true")
else:
  print("false")

#Lowercase check
s=input()
if s.islower():
  print("true")
else:
  print("false")

#String lengths equal or not
s1=input()
s2=input()
if len(s1) == len(s2):
  print("true")
else:
  print("false")

#Reverse a string
s=input()
print(s[::-1])

#Split strings by comma
s=input()
for i in s.split(","):
  print(i)

#Remove vowels
s=input()
v="aeiouAEIOU"
for char in s:
  if char in v:
    s=s.replace(char,"")
print(s)

#Reverse the character case
n=input()
print(n.swapcase())

#Print ascii value
s=input()
print(ord(s))

#Remove occurrences of a char
s=input()
char=input()
print(s.replace(char,""))

#Search for a word
sen=input()
word=input()
print("true" if word in sen else "false")

#Count vowels and consonants
s=input()
vowelcount=0
con=0
for i in s:
  if i in "aeiouAEIOU":
    vowelcount=vowelcount+1
  else:
    con=con+1 
print(vowelcount)
print(con)

#Anagram check
s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
if (len(s1)!=len(s2)):
  print("false")
elif sorted(s1)==sorted(s2):
  print("true")
else:
  print("false")

#Palindrome check
n=input()
if n==n[::-1]:
  print("true")
else:
  print("false")

