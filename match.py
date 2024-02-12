a = int(input("Enter first number: "))
op = input("Enter Operator for perform  operation (+, - , * or /): ")
b = int(input("Enter second number: "))
match op:
    case '+':
        print("The addition of the Number is",a+b) 
    case '-':
        print("The subtraction of the Number is",a-b) 
    case '*':
        print("The Multiplication of the Number is",a*b) 
    case '/':
        print("The Division of the Number is",a/b) 
    case '%':
        print("The remainder of the Number is",a%b) 
    case '**':
        print("The square of the Number is",a**b) 
    case _:
        print("Enter the corrct opertaion") 