s = input()
sum = 0
for i in range(0,len(s)):
    x = s[i]
    sum += ord(x) - 96
print(sum)
