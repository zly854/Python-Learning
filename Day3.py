# coding=utf-8
# Exercise 1
# Judge whether the number is prime

value = int(input('Please input a number: '))
flag = True
for i in range(2, int(value*0.5), 1):
    if value % 2 == 0:
        flag = False
    else:
        flag = True
if flag and value !=1:
    print('prime')
else:
    print('not prime')

# a stupid wrong: value % 2 and 2 % value

#Exercise 2
#Calculate the max factor and least common multiple

value_1=int(input('Please input the first number '))
value_2=int(input('Please input the second number '))

if value_1>=value_2:
    temp_f=value_2
    temp_m=value_1
else:
    temp_f=value_1
    temp_m=value_2

M_factor=1
for i in range(2,temp_f+1):
    if value_1%i == 0 and value_2%i ==0:
        M_factor=i
M_multiple=temp_m
for i in range(temp_m,value_1*value_2+1):
    if i%value_1==0 and i%value_2==0:
        M_multiple=i
        break

print('The max factor is %d and the least multiple is %d' % (M_factor,M_multiple))

#swap in python x,y=y,x

row = int(input("Please input the number of the row: "))
print('The first picture')
for i in range(row):
    for j in range(i+1):
        print('*', end='')
    print()
print('The second picture')
for i in range(row):
    for j in range(row):
        if j<row-i-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print('The third picture')

for i in range(row):
    for j in range(2*row-1):
        if j<row-i-1:
            print(' ', end='')
        elif j<row+i:
            print('*', end='')
        else:
            print('',end='')
    print()


