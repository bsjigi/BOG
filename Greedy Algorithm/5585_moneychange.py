price = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
coinAmount = 0

for i in coin:
    coinAmount += price // i
    price = price % i

print(coinAmount)