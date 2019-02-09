stri = input("Enter a String \n")
x,y = 0,0
for i in range(0,len(stri)):
    if stri[i] == "L":
        x-=1
    if stri[i] == "R":
        x+=1
    if stri[i] == "U":
        y+=1
    if stri[i] == "D":
        y-=1
print(len(stri))
print(x)
print(y)
