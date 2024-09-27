N = int(input())
A = list(map(int, input().split()))
freq = dict()

for party in A:
    if party in freq.keys():
        freq[party] += 1
    else:
        freq[party] = 1

maximum = 0
answer = 0
count = 0

for key, value in freq.items():
    if value > maximum:
        maximum = value
        answer = key

for value in freq.values():
    if value == maximum:
        count += 1

if count > 1:
    print(-1)
else:
    print(answer)
