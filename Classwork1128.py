# a = int(input("Enter the number: "))
# b = int(input("Enter the second number: "))
#
# if a%b==0:
#     print ("divisible")
# else:
#     print ("not divisible")

name= "Max"
#*********************************************************
# def say_hi():
#     global name
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def say_bay():
#     name = "Tom"
#     print("Good buy", name)
#
#
# say_hi()
# say_bay()
#*********************************************************

# def outer():
#     n=5
#
#     def inner():
#
#         n=20
#         print(n)
#
#     inner()
#     print(n)
#
# outer()



# def science():
#     choice = int(input("1 - Math, 2-Physics: \n"))
#     if choice == 1:
#         print ("You are Financer")
#     else:
#         print ("You are Engineer")
#
# def human():
#     choice = int(input("1 - History, 2-Foreign Languages: \n"))
#     if choice == 1:
#         print ("You are Historic or Diplomat")
#     else:
#         print ("You are Translator")
#
# def art():
#     choice = int(nput("1 - Drawing, 2-Singing: \n"))
#     if choice == 1:
#         print ("You are Painter or Architect")
#     else:
#         print ("You are Singer or Tamada")
#
#
# def sport():
#     choice = int(input("1 - Team, 2-Individual: \n"))
#     if choice == 1:
#         print("You are Basketball player")
#     else:
#         print("You are tennis player")
#
#
# choice = int (input ("Choose your branch: \n 1 - Science, 2- Humanitarian subjects, 3-Art, 4-Sport: \n"))
# if choice == 1:
#         science()
# elif choice == 2:
#         human()
# elif choice ==3:
#         art()
# elif choice ==4:
#         sport()



# a = int(input("Please enter the number of sides: "))
# b = ["Triangle", "Fourangle","Fiveangle","Sixangle","Sevenangle","Eightangle","Nineangle","Tenangle"]
# if ((a>10) or (a<3)):
#         a=int(input(("Please enter the number between 3 and 10: ")))
#         print(b[a - 3])
# else:
#     print (b[a-3])


# HW .................................................5

# username = "user"
# password = "qwerty"
#
# user = input("Please enter the the following \n Username: \n")
# passcode = input("Password: \n")
#
# if ((username==user) or (password==passcode)):
#     print ("Authentication completed")
# else:
#     print ("Invalid login or password")

# money = int(input("Insert the amount in tenge: "))
# currency = int(input("Choose currency: \n[1]USD\n[2]EUR\n[3]RUB\n"))
# if currency == 1:
#     print(money*0.0021, " USD")
# elif currency ==2:
#     print (money*0.0021, " EUR")
# elif currency ==3:
#     print (money*0.13, "RUB")
# else:
#     print ("Invalid choice")


print("Please enter 1st coordinate: ")
n1 = int(input("x: "))
n2 = int(input("y: "))
print("Please enter 2nd coordinate: ")
n3 = int(input("x1: "))
n4 = int(input("y2: "))



i = 0
j = 0
row,col=(8,8)

c = 0
k = 0




arr = [[0 for i in range(row)] for j in range(col)]
a = True
b = True


try:
    print("\n")
    print (int(n1),int(n2),int(n3),int(n4), sep=".")
except ValueError as e:
    print ("Please type a number")
except TypeError as t:
    print ("Please enter a integer")
finally:
    print("finished\n")



if (int(n1)>8 or int(n2)>8)or(int(n3>8) or int(n4>8)):
    print ("Please enter a number betweeb 1 and 8: ")
    quit()


while c<8:

    if k==8:
        if a==True:
            a=False
        else:
            a=True
        if b == True:
            b = False
        else:
            b= True
        k=0
        c=c+1
    elif (k%2==0):
        if a==True:
            arr[k][c]="W"
            k = k+1
        else:
            arr[k][c] = "B"
            k = k + 1
            a==True
    elif (k%2==1):
        if b == True:
            arr[k][c] = "B"
            k = k + 1
        else:
            arr[k][c] = "W"
            k = k + 1
            b==True


for row in arr:
    print (row)

if arr[n2-1][n1-1]==arr[n4-1][n3-1]:
    print ("Yes")
else:
    print ("No")

if (n1-1)==(n3-1) and ((n2-1)==(n4-1)):
    print ("Eats")
else:
    print ("It doesn't eat")

d1 = (n1-n3)
d2 = (n2-n4)


if ((d1==1) or (d1==-1) or (d1==0)):
    if (d2==1) or (d2==-1) or (d2 ==0):
        print("Yes")

    else:
        print("No")
else:
    print ("No")








