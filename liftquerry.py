t = int(input())
a = 0
b = 7
for i in range(t):
    n = int(input())
    if abs(a - n) > abs(b - n):
        print("B")
        b = n
    else:
        print("A")
        a = n    


    

    