size = int(input())
l = list(map(int, input().split()))
max = 0

for i in range(len(l) - size + 1):
    k = 1
    for j in l[i:i + size]:
        k *= j
    if k > max:
        max = k

print(max)
