#write a program to check a number add or even
"""
a= int(input("Enter a number for check odd or even"))
if a%2==0:
    print("The number is even number")
else:
    print("The number is odd number") 
""" 
#wap to addition of two number 
"""a = int(input("Enter the a number "))          
b = int(input("Enter the a number "))  
c=a+b
print("The addition of the two number is ",c)"""
# write a program to check the number is prime or not  
"""a = int(input("Enter the any number"))
count=1
for i in range(1,a):
    if (a % i) == 0:
        count += 1
if count==2:
    print("The Number is Prime Number")
else:
    print("The number is not prime number")"""  
#Write a program for print the sum of the first  n natural numbers.where n is given by user
"""a = int(input("Enter the a Number for  find the Sum of Natural Numbers :"))
sum_of_natural_numbers=(a*(a+1))//2
print("Sum of Natural Numbers are",sum_of_natural_numbers)"""
# alternate approach  of sum of first n natural number
"""n = int(input("Enter the any number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of the first N Number :",sum)"""    
    

#Write a program to check whether a number is leap year or not
"""year = int(input('Enter Year : '))
if ((year % 4 == 0 and year % 100 != 0)):
    print(f'{year} is a Leap Year')
elif (year % 400 == 0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is Not a Leap Year')"""
    
# write a program for print the fibonacci series of the any number 
"""a = int(input("Enter any number to print the Fibonacci series: "))

x = 0
y = 1

for i in range(a):
    print(x, end=" ")
    x, y = y, x + y
"""
# write a program to print  all odd number between 1 to n in given range 
n = int(input("Enter the value of n: "))
print("Odd numbers between 1 and", n, "are:")
for num in range(1, n + 1, 2):
    print(num, end=" ")
 

    