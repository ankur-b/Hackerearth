n = int(input())
j = input()
num = list(map(int, j.split()))
last=0
count=1
while(last+count+1)<n:
    count=count+1
    last=last+count
total = sum(num[0:last+1])
max = total
for i in range(1,n):
    if(last+1<n):
        total=total-num[i-1]+num[last+1]
        last=last+1
    else:
        total=total-num[i-1]-sum(num[(last-count+2):(last+1)])
        last=last-count+1
        count=count-1
    if total>max:
        max=total
print(max)
