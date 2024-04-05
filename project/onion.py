#BILLING SYSTEM By harshad

note='''Dear <customer> \n
THANK YOU SOO MUCH \n
FOR BUYING KANDE FROM\n
OUR SHOP\n
ON
<date>\n
AMOUNT=amount
WISH YOU A GOOD DAY!!!!'''

a=input("ENTER CUSTOMER NAME:")
b=input("ENTER DATE :")
c=input("ENTER AMOUNT :")

note=note.replace("customer",a)
note=note.replace("date",b)
note=note.replace("amount",c)

print(note)