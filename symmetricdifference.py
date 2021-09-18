n = int(input())
map1 = list(map(int, input().strip().split()))[:n]
map1 = set(map1)
n = int(input())
map2 =list( map(int, input().strip().split()))[:n]
map2 = set(map2)
dif = []
dif = list(map1.difference(map2))
dif += list(map2.difference(map1))
dif = sorted(dif)
for i in range(len(dif)):
    print(dif[i])
