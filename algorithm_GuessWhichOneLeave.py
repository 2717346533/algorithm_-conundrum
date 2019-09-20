# 生成所有组合（该函数用客人数量和客人列表作为输入参数，遍历）
def Combinations(n,guestList):
    allCombL =  []
    for i in range(2**n):
        num = i
        cList = []
        for j in range(n):
            if num % 2 == 1:
                cList = [guestList[n - 1 - j]] + cList
            num = num//2
        allCombL.append(cList)
    return allCombL

# 移除不友好的组合
def removeBadCombinations(allCombL,dislikePairs):
    allGoodCombinations = []
    for i in allCombL:
        good = True
        for j in dislikePairs:
            if j[0] in i and j[1] in i:
                good = False
        if good:
            allGoodCombinations.append(i)
    return allGoodCombinations

# 选择最大组合
def InviteDinner(guestList,dislikePairs):
    allCombL = Combinations(len(guestList),guestList)
    allGoodCombinations =  \
        removeBadCombinations(allCombL,dislikePairs)
    invite = [] # 迭代所有理想的组合，找出客人数最多的组合
    for i in allGoodCombinations:
        if len(i) > len(invite):
            invite = i
    # 等同于 invite = max(allGoodCombinations,key = len)
    print('Optimum Solution:',invite)

guestList = ['a','b','c','d','e','f','g','h','i'] # 客人列表
dislikePairs = [['b','c'],['c','d'],['d','e'],['f','g'],['f','h'],['f','i'],['g','h']] #不友好关系
InviteDinner(guestList,dislikePairs)

