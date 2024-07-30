#calculator
print("******Pooji's Calculator***")

while True:
    print()
    print("Enter Your Choose")
    print("1.Add, 2.Sub,3.Multi,4.Division")
    userinput = int(input())
    if userinput == 1:
        a=int(input("Enter 1st Number: "))
        b=int(input("Enter 2st Number: "))
        print(a+b)
    elif userinput == 2:
        a=int(input("Enter 1st Number: "))
        b=int(input("Enter 2st Number: "))
        print(a-b)    
    elif userinput == 3:
        a=int(input("Enter 1st Number: "))
        b=int(input("Enter 2st Number: "))
        print(a*b)    
    elif userinput == 4:
        a=int(input("Enter 1st Number: "))
        b=int(input("Enter 2st Number: "))
        print(a/b)
    else:
        print("Please Enter Vaild Input")
