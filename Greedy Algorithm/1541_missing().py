cal = input().split('-')

newlst = []
for i in cal:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    newlst.append(cnt)

result = newlst[0]

for i in range(1, len(newlst)):
    result = result - newlst[i]

print(result)