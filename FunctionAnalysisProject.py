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

for x in range(i1, i2+1):
    list = []
    y = eval(f)
    list.append(y)
    print("f(",x,") =", y)
    
print(list)
    
    

