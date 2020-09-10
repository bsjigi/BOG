num = input()

numlst = list(map(int, num))
numlst.sort()

sum_num = sum(numlst)
string = ''
if(numlst[0]==0) and sum_num % 3 == 0:
    for i in numlst:
        string = str(i) + string
    print(int(string))
else:
    print('-1')