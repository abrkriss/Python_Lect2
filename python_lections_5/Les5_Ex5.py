# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def _current(n):
    return n * (n + 1) / 2


def _pro(n):
    for i in range(n):
        if _current(n + 1) == (n + 1) * (n + 2) / 2:
            return True
        return False


print(_pro(5))
