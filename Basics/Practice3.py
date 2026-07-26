#Q1
n=int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")  

#Q2
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if n1>n2 and n1>n3:
    print("The greatest number is :",n1)
elif n2>n1 and n2>n3:
    print("The greatest number is :",n2)
else:
    print("The greatest number is :",n3)

#Q3
n4=int(input("Enter a number: "))
if n4%7==0:
    print("Multiple of 7 ")
else:
    print("Not a multiple of 7")