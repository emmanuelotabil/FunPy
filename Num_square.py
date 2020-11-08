result = {}

num = int(input('How many squares will you like to determine: '))

for key in range(1,num+1):
    value = key*key
    result[key]=value

for key,value in result.items():
    print('\n-',key,'----',value)