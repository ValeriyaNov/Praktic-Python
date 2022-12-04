count = 0
k = 1
for i in range(0,len(str1) - len(str2),k):
    if str2 in str1[i:i+len(str2)]:
        count += 1
        k = len(str2)
    else:
        k = 1
print(f"Вторая строка входит в первую {count} раз(а).")
