matchsticks = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
n = int(input())
for i in range(n):
    stri = input()
    scount = sum(map(matchsticks.get, stri))
    quotient, remainder = divmod(scount, 2)
    print('7' * remainder + '1' * (quotient - remainder))
