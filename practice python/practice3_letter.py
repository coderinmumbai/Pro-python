 
letter='''Dear <|name|>\n
You are selected !\n
<|date|>'''

a=input("Enter the name ") 
b=input("Enter the date ")

#here not to use print
letter=letter.replace("name",a)
letter=letter.replace("date",b)

print(letter)