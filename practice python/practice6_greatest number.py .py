a1=int(input("ENTER NUMBER 1:"))
a2=int(input("ENTER NUMBER 2:"))
a3=int(input("ENTER NUMBER 3:"))
a4=int(input("ENTER NUMBER 4:"))


#1 and 4 chi match
if(a1>a4):
    new1=a1  #here new variable is created 
else:
    new1=a4  #ithe mothi value store 

#------------------------------------------------------------------

#2 and 3 chi match 
if (a2>a3):
    new2=a2
else:
    new2=a3

#----------------------------------------------------

if(new1>new2):
    print(new1 ,"is greatest")
else:
    print(new2,"is greatest")