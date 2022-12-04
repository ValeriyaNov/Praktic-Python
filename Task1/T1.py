# a = 5
# if a>3:
#     print(123)
# elif a>1:
#     print(555)
# else:
#     print(444)

# print("Введите число");
# a=int(input());
# print("Введите число");
# b=int(input());


# if a**2 == b or b**2 == a:
#     print('yes');
# else:
#     print('no')


#Максимальное число из 5
# max_number = float('-inf')

# for i in range(1, 6):
#     number = int(input(f'Введите число {i}: '))
#     if number > max_number:
#         max_number = number

# print(max_number)

# вводи число и от -число до число
# print('n');
# n=abs(int(input()));
# for i in range(-n, n+1):
#     print(i)
n = float(input('введите число: '))
if n % 1 == 0:
    print('нет')
else:
    n1 = int(n % 1 * 10)
print(n1)


