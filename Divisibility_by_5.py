values = []

numbers = input('Enter comma separated binary numbers: ')

numbers = numbers.split(',')

for num in numbers:
    x = str(num)
    int_num = int(x,2)
    if int_num % 5==0:
        values.append(num)

print('The binary number(s) which is/are divisible by 5 when converted to decimal are: ',values)