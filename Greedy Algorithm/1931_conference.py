N = int(input())
timeList = []
countList = []

count = 0
endTime = 0
for i in range(N):
    lst = list(map(int, input().split()))
    timeList.append(lst)

timeList = sorted(timeList, key = lambda x: (x[1], x[0]))


for i in range(N):
    if endTime <= timeList[i][0]:
        endTime = timeList[i][1]
        count += 1

print(count)