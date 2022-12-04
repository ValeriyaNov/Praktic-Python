# Проверка на наличиt числа в списке строк

number = int(input(f"{''}"))
for item in lst:
    if item.isdigit():
         if int(item) == number:
            print('yes')
            break
