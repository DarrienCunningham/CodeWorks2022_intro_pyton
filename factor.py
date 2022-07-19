range = range(2000,3200)
list = []

for num in range:
    if num % 7 == 0 and num % 5 != 0:
        list.append(num)
        print(num)
