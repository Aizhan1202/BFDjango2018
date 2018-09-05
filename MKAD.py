v = int(input())
t = int(input())
s = v*t
if s > 0 and s <= 109:
    k = s
elif s > 0 and s > 109:
    k = s - 109
elif s < 0 and s*(-1) <= 109:
    k = 109 + s
elif s < 0 and s*(-1) <= 109:
    k = (109 + s)*(-1)
print(k)