print('\t\tIn this program, we will determine the factorial of some numbers.')

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input('Enter a number to determine its factorial: '))

print (fact(x))