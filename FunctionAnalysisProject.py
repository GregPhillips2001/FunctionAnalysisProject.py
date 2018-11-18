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

x= i1
len = 100
delx = (i2 - i1)/len

list = []
for i in range(0,len+1):
    y = eval(f)
    list.append(y)
    #print("f(",x,") =", y)
    x += delx
#print(list)

h = .001   
list2 = []
delxx = delx + h
x = i1 + h 
for i in range(0,len+1):
    y = eval(f)
    list2.append(y)
    #print("f(",x,") =", y)
    x += delxx
#print(list2)

list3 = []
#len = i2-i1
for i in range(0,len+1):
    der = (list2[i]-list[i])/h
    list3.append(der)
    #print("the slope is", der)
#print(list3)

list4 = []
list5 = []
list6 = []
list7 = []
x= i1
delx = (i2 - i1)/len
for i in range(0,len+1):
    y = list3[i]
    x += delx
    if y > 0:
        list4.append("+")
        list5.append(x)
    elif y < 0:
        list4.append("-")
        list6.append(x)
    else:
        list4.append("0")
        list7.append(x)
#print(list4)
#print("the function is increasing at the x values", list5)
#print("the function is decreasing at the x values", list6)
#print("the function has critical points at the x values", list7)

#for i in range(0
list8 = []
x = i1
for i in range(0,len):
    x += delx
    if list3[i] < 0 and list3[i+1] > 0:
        min = (2*x+delx)/2
        list8.append(min)
        print("There is a minimum around x = ", min)
        
x = i1
for i in range(0,len):
    x += delx
    if list3[i] > 0 and list3[i+1] < 0:
        max = (2*x+delx)/2
        list8.append(max)
        print("There is a minimum around x = ", max)

len2 = list8.amount
#for i in range(0,len2+1):
    


