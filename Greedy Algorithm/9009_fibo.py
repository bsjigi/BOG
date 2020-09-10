p = [1,2]
for i in range(2,46):
    p.append(p[i-2]+p[i-1])
T = int(input())

for i in range(T):
    n = int(input())
    result = []
    while(n!=0):
        for j in range(46):
            if(p[j] <= n):
                t = p[j]
        n -= t
        result.append(t)
    result.sort()
    for k in range(len(result)):
        print(result[k], end=' ')
    print('')
