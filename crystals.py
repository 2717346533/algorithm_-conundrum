# 检测楼层的坚固系数，n是楼层数，d是球数，
def howHardIsTheCrystal(n,d):
    r = 1
    while(r**d <= n):
        r = r + 1
    print('Radix chosen is',r)
    numDrops = 0
    floorNoBreak = [0] * d
    for i in range(d):
        for j in range(r-1):
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r,d,floorNoBreak)
            if Floor > n:
                floorNoBreak[i] -= 1
                break
            print('Drop ball',i+1,'from Floor',Floor)
            yes = input('Did the ball break (yes/no)?.:')
            numDrops += 1
            if yes == 'yes':
                floorNoBreak[i] -= 1
                break
    hardness = convertToDecimal(r,d,floorNoBreak)
    return hardness,numDrops
# 返回等价的十进制表示
def convertToDecimal(r,d,rep):
    number = 0
    for i in range(d - 1):
        number = (number + rep[i]) * r
    number += rep[d - 1]
    return number

howHardIsTheCrystal(128,4)