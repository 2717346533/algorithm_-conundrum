#假币列表
coinsList = [10,10,10,10,10,10,10,10,10,
             10,10,10,10,10,10,10,10,10,
             10,10,10,10,10,10,11,10,10]

# 比较重量的函数
def compare(groupA,groupB):
    if sum(groupA) > sum(groupB):
        result = 'left'
    elif sum(groupB) > sum(groupA):
        result = 'right'
    elif sum(groupB) == sum(groupA):
        result = 'equal'
    return result

# 给出一个硬币的列表，我们可以将列表拆分为等大的3组
def splitCoins(coinsList):
    length = len(coinsList)
    group1 = coinsList[0:length//3]
    group2 = coinsList[length//3:length//3*2]
    group3 = coinsList[length//3*2:length]
    return group1,group2,group3

# 第一次比较，确定那组有假币
def findFakeGroup(group1,group2,group3):
    resultland2 = compare(group1,group2)
    if resultland2 == 'left':
        # 当不知道假币比真币更轻或者更重的时候
        # resultland3 = compare(group1,group3)
        # if resultland3 == 'left':
        #     fakeGroup = group1
        #     type = 'heavier'
        # elif resultland3 == 'equal':
        #     fakeGroup = group2
        #     type = 'lighter'
        fakeGroup = group1
    elif resultland2 == 'right':
        fakeGroup = group2
    elif resultland2 == 'equal':
        fakeGroup = group3
    return fakeGroup

# 分治算法
def CoinComparsion(coinsList):
    counter = 0 # 用于统计要执行的称重次数
    currList = coinsList # 创建对coinsList的新引用
    while len(currList) > 1: # 分治策略，每次迭代将coinsList的长度缩小为原来的三分之一
        group1,group2,group3 = splitCoins(currList)
        currList = findFakeGroup(group1,group2,group3)
        counter += 1
    fake = currList[0]
    print('The fake coin is coin',coinsList.index(fake) + 1,' in the original list')
    print('Number of weighings:',counter)


# 开始进行称重
CoinComparsion(coinsList)