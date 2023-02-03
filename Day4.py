# coding=utf-8

# Exercise 1
# find specific number
# print('The number is:')
# for x in range(1, 1000):
#    if (x % 10)**3+((x/10) % 10)**3+((x/100) % 10) == x:
#        print('%d' % (x))

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# Exercise 2
# reverse a number
# good solution

value = int(input('Please input the number: '))
reversed_value = 0
while value > 0:
    reversed_value = reversed_value*10+value % 10
    value = value // 10

print(reversed_value)

# Exercise 3

for big_chiken in range(1, 20):
    for mid_chiken in range(1, 33):
        if (100-big_chiken-mid_chiken) % 3 == 0:
            if 5*big_chiken+3*mid_chiken+(100-big_chiken-mid_chiken)/3 == 100:
                print('Possible big_chicken is %d' % big_chiken)
                print('Possible mid_chicken is %d' % mid_chiken)
                print('Possible small_chicken is %d' %
                      (100-mid_chiken-big_chiken))


# Exercise 5
# Fibonacci sequence

value_a = 1
value_b = 1
print('1: %d' % value_a)
print('2: %d' % value_b)
for x in range(3, 21):
    value_a = value_a+value_b
    print('%d: %d' % (x, value_a))
    value_a, value_b = value_b, value_a


# Exercise 6
# perfect number


for i in range(3, 1001):
    sum = 1
    for j in range(2, i):
        if i % j == 0:
            sum = sum+j
    if sum == i:
        print(i)


# Exercise 7
# output prime number
is_prime = True
for i in range(2, 101):
    for j in range(2, i-1):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        print(i)
