bricks = input()
i = 1
while(int(bricks)>0):
    bricks = int(bricks) - i
    if(bricks<=0):
        print("Patlu")
        break
    bricks = int(bricks) - i * 2
    if(bricks<=0):
        print("Motu")
        break
    i+=1
