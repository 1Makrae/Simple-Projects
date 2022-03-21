def Main():
    fib(10)

def fib(length):
    if (length == 0):
        print([])
        return
    fibarray = [1]
    printNum = 1
    print(1)
    Fibonacci1 = 0
    Fibonacci2 = 1
    stop = False
    while not stop:
        if (printNum == length):
            print(fibarray)
            break
        elif (printNum <= length):
            printer = Fibonacci1 + Fibonacci2
            printNum = printNum + 1
            Fibonacci1 = printer
            fibarray = fibarray + [printer]
        if (printNum == length):
            print(fibarray)
            break
        elif (printNum <= length):
            printer = Fibonacci1 + Fibonacci2
            printNum = printNum + 1
            Fibonacci2 = printer
            fibarray = fibarray + [printer]

Main()