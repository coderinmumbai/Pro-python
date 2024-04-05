# Program to display the Fibonacci sequence up to n-th term

a = int(input("Enter the number : "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if a <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < a:
       print(n1)
       c = n1 + n2
       # update values
       n1 = n2
       n2 = c
       count += 1