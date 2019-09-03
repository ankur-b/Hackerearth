t = int(input())
for i in range(t):
    n = int(input())
    flag = False
    while n > 1:
        if n == 1:
            flag = True
        else:   
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
    print("YES") if n == 1 else print("NO")        

