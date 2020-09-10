import sys
input = sys.stdin.readline

price = []
singleList = []
line, brand = map(int, input().split())
for i in range(brand):
    six, single = map(int, input().split())
    price.append((six, single))

price.sort()
money = 0
six_point = price[0][0]
for i in price:
    singleList.append(i[1])
single_point = min(singleList)
if six_point > (single_point*6):
    six_point = (single_point*6)
while(line > 0):
    if line >= 6:
        money = money + six_point
        line = line - 6
    else:
        if six_point > (single_point*line):
            money = money + (single_point*line)
            line = 0
        else:
            money = money + six_point
            line = 0
print(money)