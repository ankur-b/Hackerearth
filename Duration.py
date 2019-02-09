n = int(input())

while(n>0):
    sh,sm,eh,em = input().split()
    x = int(eh) * 60 + int(em) - int(sh) * 60 - int(sm)
    h = x // 60
    m = x % 60
    print(str(h) +" "+str(m))
    n-=1
