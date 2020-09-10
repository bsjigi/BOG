t = int(input())
word = [list(map(lambda x: ord(x)-65, input())) for _ in range(t)]
alpha = [0] * 26


for i in range(t):
    j = 0
    for w in word[i][::-1]:
        alpha[w] += (10 ** j)
        j += 1

alpha.sort(reverse=True)
ans = 0
maxNum = 9
for i in range(26):
    if alpha[i] == 0:
        break
    ans += (maxNum * alpha[i])
    maxNum -= 1

print(ans)