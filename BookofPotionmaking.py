pos = input()

if len(pos) == 10:
    sum = 1 * int(pos[0]) + 2 * int(pos[1]) + 3 * int(pos[2]) + 4 * int(pos[3]) + 5 * int(pos[4]) + 6 * int(pos[5]) + 7 * int(pos[6]) + 8 * int(pos[7]) + 9 * int(pos[8]) + 10 * int(pos[9])
    if sum % 11 == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")
