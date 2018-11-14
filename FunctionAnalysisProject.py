#Greg Phillips and Andrew Enelow
#FunctionAnalysisProject.py
#11/16/18

from math import *
from random import randint

print("Enter a function (in terms of x): ")
f = input("")

print("Enter the left point of the interval: ")
i1 = int(input(""))
print("Enter the right point of the interval: ")
i2 = int(input(""))

list = []
for x in range(i1,i2+1):
    y = eval(f)
    list.append(y)
    print("f(",x,") =", y)
print(list)

h = .001   
list2 = []
for x in range(i1,i2+1):
    x += h
    y = eval(f)
    list2.append(y)
    print("f(",x,") =", y)
print(list2)

list3 = []
len = i2-i1
for i in range(0,len+1):
    der = (list2[i]-list[i])/h
    list3.append(der)
    print("the slope is", der)
print(list3)

list4 = []
list5 = []
list6 = []
list7 = []
x= i1
for i in range(0,len+1):
    y = list3[i]
    x += 1
    if y > 0:
        list4.append("+")
        list5.append(x)
    elif y < 0:
        list4.append("-")
        list6.append(x)
    else:
        list4.append("0")
        list7.append(x)
print(list4)
print("the function is increasing at the x values", list5)
print("the function is decreasing at the x values", list6)
print("the function has critical points at the x values", list7)

