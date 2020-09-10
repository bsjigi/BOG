list = [300, 60, 10]
time = int(input())
ans = []
for i in list:
    count = time // i
    time = time - (i*count)
    ans.append(count)

if time != 0:
    print(-1)
else:
    for i in ans:
        print(i, end=' ')

