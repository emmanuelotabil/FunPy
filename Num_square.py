result = {}

print('\t\tIn this program, we will print out the squares of numbers in a given range.')

num_1 = int(input('\n\nEnter lower limit of range: '))

num_2 = int(input('\n\nEnter upper limit of range: '))


for key in range(num_1,num_2+1):
    result[key] = key * key

for key,value in result.items():
    print('\n-',key,'----',value)