num = int(input())
lst = list(map(int, input().split()))
total = 0
time = 0

for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(num):
    total = total + lst[i]
    time = time + total

print(time)