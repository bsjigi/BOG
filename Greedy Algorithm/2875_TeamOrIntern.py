w, m, it = map(int, input().split())

t = 0
while True:

    if t*2 <= w and t <= m and (t*2)+t <= (w+m-it):
        t += 1
    else:
        print(t-1)
        break

