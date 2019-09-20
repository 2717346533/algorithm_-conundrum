# 迭代查找
def findSquareRoot(x):# 定义函数，参数x
    if x < 0: # 检查x >= 0
        print('Sorry,no imaginary numbers!')
        return
    ans = 0
    while ans**2 < x:
        ans = ans + 1
    if ans**2 != x:
        print(x,"is not a perfect square")
        print('Square root of ' + str(x) + ' is close to ' + str(ans - 1))
    else:
        print('Square root of ' + str(x) + ' is ' + str(ans)) # 整数平方根

# findSquareRoot(65535)

# 允许用户来决定平方根的误差值是多少
def findSquareRootWithinError(x,epsilon,increment):
    if x < 0:
        print('Sorry,no imaginary numbers!')
        return
    numGuesses = 0
    ans = 0.0
    while x - ans**2 > epsilon:
        ans += increment
        numGuesses += 1
    print('numGuesses =',numGuesses)
    if abs(x - ans**2) > epsilon:
        print('Failed on square root of',x)
    else:
        print(ans,'is close to square root of',x)

# findSquareRootWithinError(65535, .1, .001)

# 折半查找
def bisectionSearchForSquareRoot(x,epsilon):
    if x < 0:
        print('Sorry,imaginary numbers are out of scope!')
        return
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        numGuesses += 1
    print('numGuesses = ',numGuesses)
    print(ans,'is close to square root of',x)

# bisectionSearchForSquareRoot(65535, .01)

# 按顺序检查
NOTFOUND = -1
Ls = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def lsearch(L,value):
    for i in range(len(L)):
        if L[i] == value:
            return i
    return NOTFOUND

# lsearch(Ls,13)

# 二分搜索
def bsearch(L,value):
    lo,hi = 0,len(L) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if L[mid] < value:
            lo = mid + 1
        elif value < L[mid]:
            hi = mid - 1
        else:
            print(mid)
    return NOTFOUND

# 三分搜索
# 假币谜题（谜题6）