num=int(input("ENTER NUMBER\n"))
#here we are assuming that it a prime number thats why true 
prime=True
for a in range(2,num):  #<--- 2 bcoz ithun start

#jar kontaa pn number hyala divide marlaa trr number prime nasnrr 
    if (num%a == 0):
        prime=False
        break

#-----------------
if prime:
    print("prime number")
else:
    print("not prime")