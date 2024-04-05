a = int(input("Enter the number of elements \n")) 
b= []
for i in range(a):
    val = input(("Enter the element ")) 
    b.append(val)
print(b)

b.sort(key = len,reverse = True) 
print(b)