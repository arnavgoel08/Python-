a="This is a string"
b=' .Arnav'
c=""" .This is another string"""

str = a+b+c
print(str)
print("Length of string is :",len(str))
print(str[15])
print(str[31])
print(str[1:5])
print(str[1:len(str)])
print(str.endswith("ing"))
print(str.capitalize())
print(str.replace("string","STRING"))
print(str.find("string"))
print(str.count("string"))