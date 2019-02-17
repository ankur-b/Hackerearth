n=int(input())
for x in range(n):
    s=input()
    l=len(s)
    sum=0
    for i in range(l):
        if s[i] in "aeiouAEIOU":
            sum+=(i+1)*(l-i)
    print(sum)
