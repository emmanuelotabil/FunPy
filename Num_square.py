result = {}
#Program description
print('\t\tIn this program, we will print out the squares of numbers in a given range.')

#Get user input for upper and lower limits
num_1 = int(input('\n\nEnter lower limit of range: '))

num_2 = int(input('\n\nEnter upper limit of range: '))

#Calculate squares
for key in range(num_1,num_2+1):
    result[key] = key * key

#Print output in a formatted way.
for key,value in result.items():
    print('\n-',key,'----',value)