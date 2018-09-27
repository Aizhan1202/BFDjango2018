n = int(input())
if n == 1:
    print("Yes")
elif n%2 != 0:
    print("No")
while n%2 == 0:
    n = n/2
if n == 1:
    print("Yes")
else:
    print("No")