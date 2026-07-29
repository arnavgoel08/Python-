#Q1
n1=input("Enter the name of your first favorite movie ")
n2=input("Enter the name of your second favorite movie ")
n3=input("Enter the name of your third favorite movie ")
movies=[n1,n2,n3]
print(movies)

#Q2
l=[1,2,3,4,5,4,3,2]
l1=l.copy()
l1.reverse()
if l==l1:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

#Q3
tuple=("C","D","A","A","B","B","B","A")
print(tuple.count("A"))

list=["C","D","A","A","B","B","B","A"]
list.sort()
print(list)