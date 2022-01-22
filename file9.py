import os
from flask import Flask
app = Flask(_name_)
l= []
n=int(input("entre the number of elements : "))
i=0
while(i<n):
 v=int(input())
 l.append( v)
 i+=1

x=input(" A or D or N  ")
if (x == "A"):
  l.sort()
  print(l)
elif (x == "D"):
 l.sort()
 l.reverse()
 print(l)
else:
 print(l)

