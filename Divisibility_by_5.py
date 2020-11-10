
#Create empty ist to store values
values = []

#Get user input of comma separated binary numbers
numbers = input('Enter comma separated binary numbers: ')

numbers = numbers.split(',')

#Check their divisibility by 5
for num in numbers:
    x = str(num)
    int_num = int(x,2)
    if int_num % 5==0:
        values.append(num)

#Print outcome
print('\n\nThe binary number(s) which is/are divisible by 5 when converted to decimal are: \n',values)