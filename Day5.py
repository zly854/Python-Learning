
def main():
    def gcd(a, b):
        if a > b:
            a, b = b, a
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                value = i
        return value

    print(gcd(9, 15))

    def lcm(a, b):
        if a > b:
            a, b = b, a
        for i in range(b, a*b+1):
            if i % a == 0 and i % b == 0:
                value = i
                break
        return value
    print(lcm(15, 6))
    def is_not(number):
        temp = number
        reserve = 0
        while (temp > 0):
            reserve = reserve*10+temp % 10
            temp = temp//10
        if reserve == number:
            return True
        else:
            return False
    print(is_not(12321))
    def is_prime(number):
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                flag = False
                break
            else:
                flag = True
        return flag
    print(is_prime(29))
    def double_judge(number):
        if is_prime(number) and is_not(number):
            return True
        else:
            return False
    print(double_judge(121))

if __name__=='__main__':
    main()
