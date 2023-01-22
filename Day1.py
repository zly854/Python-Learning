#Exercise 1
#template conversion
a=float(input('Please input the template: '))
b=(a-32)/1.8
print('The template is %.1f ' % (b))

#some questions: python is strict with grammar,the end of the function input should be a 'space'

#Exercise 2
#Calculate the area and the perimeter of a circle
radius=float(input('Please input the radius of the circle '))
area=radius*3.1416
perimeter=2*3.1416*radius
print('The area of the circle is %.1f ' % (area) )
print('The perimeter of the circle is %.1f ' % (perimeter ))

#Exercise 3
#Judge whether the year is the leap year

year=int(input('Please input the year '))
is_leap=bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)

#Notice:logistic operator ought to be carefully remembered.

#First time to use git and there are many problems troubling me, but it's worth being happy that all problems have been solved perfectly. 





