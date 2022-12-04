# Случайные числа выводить

def time1():
    return (datetime.datetime.now().microsecond // 100 % 10) **\
        (datetime.datetime.now().microsecond % 10)


print(time1())

# 2 metod
from time import time

def randfromtime(max):
    time1 = time()
    time1 = (time1 - int(time1))
    return int(time1 * max)

print(randfromtime(1000))
