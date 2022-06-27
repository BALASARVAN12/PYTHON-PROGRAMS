def Fibonacci(n):
    if n <=1:
        return n
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))

number=int(input("How many terms of series are required? "))
for i in range(number):
    print(Fibonacci(i))
