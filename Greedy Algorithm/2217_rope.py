num = int(input())
ropeList = []
weightList = []
weight = 0
for i in range(num):
    rope = int(input())
    ropeList.append(rope)
ropeList.sort(reverse=True)
for j in range(num):
    weight = ropeList[j]*(j+1)
    weightList.append(weight)

print(max(weightList))