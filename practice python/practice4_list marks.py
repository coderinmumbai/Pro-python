#This is the another way to convert 
stud1=int(input("ENTER MARKS OF STUDENT 1 :"))
stud2=int(input("ENTER MARKS OF STUDENT 2 :"))
stud3=int(input("ENTER MARKS OF STUDENT 3 :"))
stud4=int(input("ENTER MARKS OF STUDENT 4 :"))
stud5=int(input("ENTER MARKS OF STUDENT 5 :"))
stud6=int(input("ENTER MARKS OF STUDENT 6 :"))

main_list=[stud1,stud2,stud3,stud3,stud4,stud5,stud6]
#using sort method
main_list.sort() 

print("ALL THE MARKS ENTER ARE :",main_list)