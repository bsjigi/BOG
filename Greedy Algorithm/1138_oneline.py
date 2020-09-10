n = int(input())
lst = list(map(int,input().split()))
newList = []

for i in range(n-1, -1, -1):
    newList.insert(lst[i], i+1)

for i in newList:
    print(i,end=' ')



