s1, s2 = input().split()
num = int(s1)
money = int(s2)
unitList = []
count = 0
for i in range(num):
    unit = int(input())
    unitList.append(unit)

for j in range(num-1, -1, -1):
    if money // unitList[j] >= 0:
        count = count + money // unitList[j]
        money = money - unitList[j]*(money // unitList[j])

print(count)