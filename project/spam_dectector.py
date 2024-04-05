comment=input("ENTER YOUR COMMENT :\n")
trying=comment.lower() #BY KAUSIN IDEA

if ("subscribe me" in trying):
    spam= True   #this is a variable name and a bool value 

elif("like me" in trying):
    spam=True
elif("buy now" in trying):
    spam=True
elif("make money" in trying):
    spam=True
#this is a last one
else:
    spam=False

#-------------------------------------------
if(spam is True):  #this will check it 
    print("This is a spam")
else:
    print("Thankyou")



