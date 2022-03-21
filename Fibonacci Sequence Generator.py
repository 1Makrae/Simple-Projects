def Main(length):
    fib(length)

def fib(length):
    printNum = 1
    print(1)
    Fibonacci1 = 0
    Fibonacci2 = 1
    stop = False
    while not stop:
        if (printNum == length):
            break
        elif (printNum <= length):
            printer = Fibonacci1 + Fibonacci2
            print(printer)
            printNum = printNum + 1
            Fibonacci1= printer
        if (printNum == length):
            break
        elif (printNum <= length):
            printer = Fibonacci1 + Fibonacci2
            print(printer)
            printNum = printNum + 1
            Fibonacci2= printer

