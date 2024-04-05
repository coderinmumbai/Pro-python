sub1=int(input("enter marks of maths :"))
sub2=int(input("enter marks of science :"))
sub3=int(input("enter marks history :"))


if(sub1<35 or sub2<35 or sub3<35):
    print("YOU ARE FAIL BECAUSE YOU SCORE LESS THAN 35 MARKS ")
 
elif(sub1+sub2+sub3)/300 <35:
    print("your percentage is less than 35 so you failed")


else:    
    print("congrat you are totally passed")