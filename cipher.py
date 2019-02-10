stri = input()
n = int(input())
s = ""
for i in range(0,len(stri)):
    ch = stri[i]
    if ch.isupper():
        s += chr(65+(ord(ch)+n-65) % 26)
    elif ch.islower():
        s += chr(97+(ord(ch)+n-97) % 26)
    elif ch.isnumeric():
        s += str((int(ch) + n) % 10)
    else:
        s += ch
print(s)
