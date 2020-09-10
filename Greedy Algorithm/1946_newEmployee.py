import sys
input = sys.stdin.readline
case = int(input())

for i in range(case):
    record = []
    app = int(input())
    for j in range(app):
        res, inter = map(int, input().split())
        record.append((res, inter))
    record.sort()

    cnt = 1
    point = record[0][1]

    for p in record:
        if point > p[1]:
            point = p[1]
            cnt += 1
    print(cnt)