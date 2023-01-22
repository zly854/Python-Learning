# coding=utf-8

# Exercise 1
# Units conversion

value = float(input('Please input the value '))
unit = input('Please input the unit ')

if (unit == 'in'):
    print('%.1f in equals to %.1f cm' % (value, value*2.54))
elif unit == 'cm':
    print('%.1f cm equals to %.1f in' % (value/2.54, value))
else:
    print('The unit you input is wrong')
# question1:There is a wrong when i input chinese character.
# Solution:note "# coding=utf-8" on the top of the source file
# question2:python2 doesn't support input character directly
# Solution:i dont know why i can't run the code in vs code,but the source file can be ran in terminal correctly with Python3
# question3:f-string wrong
# Solution:i can't run the code 'f{}' in vs code, but it can be ran in terminal correctly.

# Exercise2
# grade conversion

grade = float(input('Please input the grade of the student: '))
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('E')

#Exercise3
#Calculate
a=float(input('Please input the first number: '))
b=float(input('Please input the second number: '))
c=float(input('Please input the third number: '))
p=(a+b+c)/2
if a+b>c and a+c>b and b+c>a:
    print('The area and pre are: %.1f and %.1f ' % (a+b+c,(p*(p-a)*(p-b)*(p-c))**0.5))
else:
    print('Please input again')
