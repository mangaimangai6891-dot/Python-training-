#Sum of Array Elements
n=input()
arr=list(map(int, input().split()))
print(sum(arr))

#Sum of Odd and Even Elements in an Array
n=int(input())
arr=list(map(int, input().split()))
even=odd=0
for i in arr:
  if i%2 == 0:
    even += i
  else:
    odd += i
print(even, odd)

#Sum of Elements at Odd and Even Indices in an Array
n=int(input())
arr=list(map(int, input().split()))
even=0
odd=0
for i in range(n):
  if i%2 == 0:
    even += arr[i]
  else:
    odd += arr[i]
print(even, odd)

#Find Maximum Element in an Array
n=int(input())
arr=list(map(int, input().split()))
maximum=max(arr)
print(maximum)

#Find Minimum Element in an Array
n=int(input())
arr=list(map(int, input().split()))
minimum=min(arr)
print(minimum)

#Find Maximum Odd and Even Elements in an Array
import sys
size=int(input())
arr=tuple(map(int, input().split()))
oddmax=evenmax=-sys.maxsize-1
for x in arr:
  if x%2 == 0:
    if x>evenmax:
      evenmax=x
  else:
    if x > oddmax:
      oddmax=x
if evenmax==-sys.maxsize-1:
  print("None")
else:
  print(evenmax)
if oddmax==-sys.maxsize-1:
  print("None")
else:
  print(oddmax)

#Difference Between Sum of Odd and Even Elements in an Array
n=int(input())
arr=list(map(int, input().split()))
odd=0
even=0
for i in arr:
  if i%2 == 0:
    even+=i
  else:
    odd+=i
difference=odd-even
print(difference)

#Check if a Key Number Exists in an Array
n=int(input())
arr=list(map(int, input().split()))
key=int(input())
if key in arr:
  print("Yes")
else:
  print("No")

#Find Index of a Key Number in an Array
n=int(input())
s=list(map(int, input().split()))
key=int(input())
if key in s:
  print(s.index(key))
else:
  print(-1)
