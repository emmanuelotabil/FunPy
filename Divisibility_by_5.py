values = []

numbers = input('Enter your numbers: ')

numbers = numbers.split(',')

for num in numbers:
    x = str(num)
    int_num = int(x,2)
    if int_num % 5==0:
        values.append(num)

print(values)