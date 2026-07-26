age = int(input("Enter your age: "))
if age >= 18:
    print("Your eligible for driving license")
else:
    print("Your not eligible for driving license")

l=input("What is the colour of the traffic light: ")
if l=="red" or l=="Red" or l=="RED":
    print("Stop")
elif l=="yellow" or l=="Yellow" or l=="YELLOW":
    print("Get ready to move")
else:
    print("Move")