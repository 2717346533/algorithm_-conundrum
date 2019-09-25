# 每次生成并测试一个组合
def Hire4Show(candList,candTalents,talentList):
    n = len(candList)
    hire = candList[:]
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n):
            if(num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2
        if Good(Combination,candList,candTalents,talentList):
            if len(hire) > len(Combination):
                hire = Combination
    print('Optimum Solution:',hire)
    
# 确定缺少一门绝活的组合
def Good(Comb,candList,candTalents,AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False
    return True

Talents = ['Sing','Dance','Magic','Act','Flex','Code']
Candidates = ['Aly','Bob','Cal','Don','Eve','Fay']
CandidateTalents = [['Flex','Code'],['Dance','Magic'],['Sing','Magic'],['Sing','Dance'],['Dance','Act','Code'],['Act','Code']]

Hire4Show(Candidates,CandidateTalents,Talents)
