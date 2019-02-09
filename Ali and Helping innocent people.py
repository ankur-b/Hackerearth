a = input()
vovels = ["A","E","I","O","U","Y"]
check = False
if a[2] not in vovels:
    x = int(a[0]) + int(a[1])
    if x % 2 == 0:
        x = int(a[3]) + int(a[4])
        if x % 2 == 0:
            x = int(a[4]) + int(a[5])
            if x % 2 == 0:
                x = int(a[7]) + int(a[8])
                if x % 2 == 0:
                    check = True
    else:
        check = False
if check:
    print("valid")
else:
    print("invalid")
