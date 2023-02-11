import math
from decimal import Decimal

def calc_pi(epsilon):
    n = 2
    pi = 4 * [1, -1/3]
    dif = 1
    while dif > epsilon:
        pi.append(4 * (-1) ** n / (2 * n + 1))
        dif = abs(sum(pi[:-1]) - sum(pi[:-2]))
        n +=1

    return math.floor(sum(pi)*int(1/epsilon))*epsilon

def gauss_pi(d):
    accuracy = 1
    pi_gauss = 48*math.atan(1/18)+32*math.atan(1/57)-20*math.atan(1/239)
    number_of_digits = int(len(str(d).split('.')[1]))
    print(number_of_digits)
    while number_of_digits > 0:
        accuracy *=10
        number_of_digits-=1
    return int(pi_gauss*accuracy)/accuracy

def chud_seriea(n)->Decimal:
    pi = Decimal(0)
    delta = Decimal(10005).sqrt()/Decimal(4270934400)
    measure = len(str(n))-2
    for i in range(0,measure+1):
        multiplier = (13591409 + 545140134 * i)
        if i != 0:
            delta *= -Decimal((6*i-5)*(2*i-1)*(6*i-1)/Decimal(26680-640320*640320*i*i*i))
        multiplier*= delta
        pi+=multiplier
    return str(pi**-1)[:measure+2]




