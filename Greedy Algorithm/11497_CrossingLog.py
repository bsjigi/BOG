case = int(input())

for i in range(case):
    n = int(input())
    log = list(map(int,input().split()))
    log.sort()
    result = 0
    for j in range(2,n):
            c = log[j] - log[j-2]
            result = max(c,result)
    print(result)

