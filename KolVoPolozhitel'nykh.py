a = int(input())
b = list(map(int, input().split()))
k = 0
for elem in b:
    if elem > 0:
        k += 1

print(k)