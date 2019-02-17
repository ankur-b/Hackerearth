def isprime(n):
    if(n==2 or n==3):
        return True
    if(n%2==0 or n<2):
        return False
    for i in range(3,int(n**0.5)+1,2):
        if(n%i==0):
            return False
    return True
n1,n2 = map(int,input().split())
for num in range(n1,n2+1):
    if isprime(num):
        if isprime(num):
            q=num
            s=0
            while(q>0):
                s=(s+q%10)
                q=int(q/10)
        #print("s:",int(s))
            if(isprime(int(s))):
                print(num,end=" ")
