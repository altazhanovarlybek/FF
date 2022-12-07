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
