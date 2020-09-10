n = int(input())
milk = list(map(int,input().split()))
count = 0
m = 0
for i in milk:
    if i == m:
        count+=1
        m+=1
    elif m > 2:
        m = 0
        if i == m:
            count += 1
            m += 1


print(count)

