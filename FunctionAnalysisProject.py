#Greg Phillips and Andrew Enelow
#FunctionAnalysisProject.py
#11/16/18

from math import *

print("Enter a function (in terms of x): ")
f = input("")

print("Enter the left point of the interval: ")
i1 = int(input(""))
print("Enter the left point of the interval: ")
i2 = int(input(""))

list = []
for x in range(i1, i2+1):
    y = eval(f)
    list.append(y)
    print("f(",x,") =", y)
print(list)
    
list2 = []
for x in range(i1, i2+1):
    x += 0.001
    y = eval(f)
    list2.append(y)
    print("f(",x,") =", y)
print(list2)
    

