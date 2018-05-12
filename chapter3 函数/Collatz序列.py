def collatz(number):
    if number % 2 ==0:
        return number//2
    elif number % 2 == 1:
        return number*3+1
    else:
        print('error')

while True:
    keyinput = int(input())
    getnum = collatz(keyinput)
    print(getnum)
    if getnum == 1:
        break 