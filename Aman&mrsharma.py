days = int(input())
t = 0
pi = 22/7
for i in range(days):
    r, x = map(float, input().split())
    p = pi*2*r
    capacity = 100*x
    if p<capacity:
        t = t + 1
print(t)
