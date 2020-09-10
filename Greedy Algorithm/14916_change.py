n = int(input())
count = 0

if (n % 5) % 2 == 0:
    count = n // 5
    count += (n - ((n//5)* 5)) / 2
else:
    if n > 3:
        count = (n//5)-1
        count += (n - (((n//5) - 1) * 5)) / 2
    else:
        count = -1


print(int(count))