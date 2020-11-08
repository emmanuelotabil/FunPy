number = range(2000,3201)

for num in number:
    if num % 7 ==0 and num % 5 != 0:
        print('-',num)


#ALTERNATIVE SOLUTION
output = []

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        output.append(str(i))

print('\n\n\n',','.join(output))