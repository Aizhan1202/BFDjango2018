n = int(input())
s = 0
a = list(map(n, input().split()))
for i in range(0, n):
    if a[i] > 0:
        s = s + 1

print(s)