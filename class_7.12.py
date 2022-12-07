#1***************************************************************
# print ("Please enter A/B/H: \n")
#
# A = int(input("A: "))
# B = int(input("B: "))
# H = int(input("H: "))
#
# if A<H<B:
#     print("Нормально")
# elif H>B:
#     print("Пересып")
# elif H<A:
#     print("Недосып")

#2***************************************************************

# Year = int(input("Eter a year:  "))
#
# if 1900<Year<3000:
#     if  (Year%4)==0:
#         if (Year%100)==0:
#             print("Обычный")
#         else:
#             print ("Високосный")
#     else:
#         print("Обычный")
# else:
#     print ("please enter a year between 1900 and 3000")


#3***************************************************************
# integer = int(input("Please enter a whole number: "))
#
# if (-15<integer<=12) or (14<integer<17) or (19<=integer):
#     print("True")
# else:
#     print ("False")


#4***************************************************************
# import math
# pi =3.14
#
# figure = input("Тип фигуры: ")
#
#
#
# def triangle():
#     a = float(input("a: "))
#     b = float(input("b: "))
#     c = float(input("c: "))
#     s = (a+b+c)/2
#     print (math.sqrt(s*(s-a)*(s-b)*(s-c)))
# def square():
#     a = float(input("a: "))
#     b = float(input("b: "))
#     print (a*b)
# def circle():
#     r = float(input("r: "))
#     print(3.14*r*r)
#
#
# if figure == "треугольник":
#     triangle()
# elif figure == "прямоугольник":
#     square()
# elif figure == "круг":
#     circle()

#5***************************************************************

n = int(input("n: "))

if n<0:
    print("Please enter a number above zero: ")
elif n==1:
    print(n,"программист")
elif (n==0) or (n>2):
    print(n, "программистов")
elif (n==2):
    print(n, "программиста")
