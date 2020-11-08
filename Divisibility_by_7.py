number = range(2000,3201)

for num in number:
    if num % 7 ==0 and num % 5 != 0:
        print('-',num)