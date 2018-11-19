#Greg Phillips and Andrew Enelow
#FunctionAnalysisProject.py
#11/16/18

from math import *
from random import randint

#here the user is entering the function which will be evaluated
print("Enter a function (in terms of x): ")
f = input("")

#user is entering the interval in which the function is evaluated
print("Enter the left point of the interval: ")
i1 = int(input(""))
print("Enter the right point of the interval: ")
i2 = int(input(""))

x= i1
len1 = 100
delx = (i2 - i1)/len1

list = []
for i in range(0,len1+1):
    y = eval(f)
    list.append(y)
    x += delx

h = .001   
list2 = []
delxx = delx + h
x = i1 + h 
for i in range(0,len1+1):
    y = eval(f)
    list2.append(y)
    x += delxx

list3 = []
for i in range(0,len1+1):
    der = (list2[i]-list[i])/h
    list3.append(der)

x= i1
delx = (i2 - i1)/len1

list4 = []
list5 = []

if list3[0]>0:
    print("x =", i1,"is a minimum")
    list5.append(-1)
else:
    print("x =", i1,"is a maximum")
    list5.append(1)
if list3[len1]>0:
    print("x =", i2,"is a maximum")
    list5.append(1)
else:
    print("x =", i2,"is a minimum")
    list5.append(-1)

x = i1
for i in range(0,len1):
    x += delx
    if list3[i] < 0 and list3[i+1] > 0:
        min = (2*x+delx)/2
        list4.append(min)
        list5.append(-1)
        print("There is a minimum at approximately x =", round(min,2))
    elif list3[i] > 0 and list3[i+1] < 0:
        max = (2*x+delx)/2
        list4.append(max)
        list5.append(1)
        print("There is a maximum at approximately x =", round(max,2))

l = len(list4)
for i in range(0,l-1):
    if list5[i] < 0:
        print("the function is increasing from x =", round(list4[i],2), "to x =", round(list4[i+1],2))
    elif list5[i] > 0:
        print("the function is decreasing from x =", round(list4[i],2), "to x =", round(list4[i+1],2))

list6 = []
for i in range(0, len1):
    der2 = (list3[i]-list3[i+1])/h
    list6.append(der2)

l2 = len(list6)
list7 = []
list8 = []
x = i1
for i in range(0,l2-1):
    x += delx
    if list6[i] < 0 and list6[i+1] > 0:
        inf = (2*x+delx)/2
        list7.append(inf)
        list8.append(-1)
        print("There is a point of inflection at approximately x =", round(inf,2))
    elif list6[i] > 0 and list6[i+1] < 0:
        inf = (2*x+delx)/2
        list7.append(inf)
        list8.append(1)
        print("There is a point of inflection at approximately x =", round(inf,2))

l3 = len(list7)
if l3 > 0:
    for i in range(0,l-1):
        if list8[i] < 0:
            print("The function is concave up from x =", round(list7[i],2), "to x =", round(list7[i+1],2))
        elif list8[i] > 0:
            print("The function is concave down from x =", round(list7[i],2), "to x =", round(list7[i+1],2))
else:
    print("There are no points of inflection")
    if list6[1]>0:
        print("The function is always concave up")
    else:
        print("The function is always concave down")


