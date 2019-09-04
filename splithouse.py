n = int(input())
str = input()
if 'HH' in str:
    print("NO")
elif len(str)==1 or '.' in str:
    print("YES")
    print(str.replace(".","B"))
else:
    print("NO")