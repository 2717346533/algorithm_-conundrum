# 扑克牌
deck=['A_C','A_D','A_H','A_S','2_C','2_D','2_H','2_S',
'3_C','3_D','3_H','3_S','4_C','4_D','4_H','4_S',
'5_C','5_D','5_H','5_S','6_C','6_D','6_H','6_S',
'7_C','7_D','7_H','7_S','8_C','8_D','8_H','8_S',
'9_C','9_D','9_H','9_S','10_C','10_D','10_H','10_S',
'J_C','J_D','J_H','J_S','Q_C','Q_D','Q_H','Q_S',
'K_C','K_D','K_H','K_S'
]
# 助手的工作
def AssistantOrdersCards():
    print('Cards are character strings as shown below.')
    print('Ordering is:',deck)
    cards,cind,cardsuits,cnumbers = [],[],[],[]
    numsuits = [0,0,0,0]
    for i in range(5):
        print('Please give card',i+1,end=' ')
        card = input('in above format:')
        cards.append(card)
        n=deck.index(card)
        cind.append(n)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)
    hidden,other,encode = \
        outputFirstCard(cnumbers,cardh,cards)
    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    sortList(remindices)
    outputNext3Cards(encode,remindices)
    return

# 确定两张牌中的那些作为隐藏牌
def outputFirstCard(ns,oneTwo,cards):
    encode = (ns[oneTwo[0]] - ns[oneTwo[1]]) % 13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (ns[oneTwo[1]] - ns[oneTwo[0]]) % 13
    print('First card is:',cards[other])
    return hidden,other,encode

# 对列表ind所保存的其余三张牌做排序
def outputNext3Cards(code,ind):
    if code == 1:
        s,t,f = ind[0],ind[1],ind[2]
    elif code == 2:
        s, t, f = ind[0], ind[2], ind[1]
    elif code == 3:
        s, t, f = ind[1], ind[0], ind[2]
    elif code == 4:
        s, t, f = ind[1], ind[2], ind[0]
    elif code == 5:
        s, t, f = ind[2], ind[0], ind[1]
    else:
        s, t, f = ind[2], ind[1], ind[0]
    print('Second card is:',deck[s])
    print('Third card is:',deck[t])
    print('Fourth card is:',deck[f])

# 排序过程
def sortList(tlist):
    for ind in range(0,len(tlist) - 1):
        iSm = ind
        for i in range(ind,len(tlist)):
            if tlist[iSm] > tlist[i]:
                iSm = i
        tlist[ind],tlist[iSm] = tlist[iSm],tlist[ind]

# 魔术师
def MagicianGuessesCard():
    print('Cards are character strings as shown below.')
    print('Ordering is:',deck)
    cards,cind = [],[]
    for i in range(4):
        print('Please give card',i+1,end=' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        if i == 0:
            suit = n % 4
            number = n // 4
            if cind[1] < cind[2] and cind[1] < cind[3]:
                if cind[2] < cind[3]:
                    encode = 1
                else:
                    encode = 2
            elif ((cind[1] < cind[2] and cind[1] > cind[3])
            or (cind[1] > cind[2] and cind[1] < cind[3])):
                if cind[2] < cind[3]:
                    encode = 3
                else:
                    encode = 4
            elif cind[1] > cind[2] and cind[1] > cind[3]:
                if cind[2] < cind[3]:
                    encode = 5
                else:
                    encode = 6
            hiddennumber = (number + encode) % 13
            index = hiddennumber * 4 + suit
            print('Hidden card is:' + deck(index))

AssistantOrdersCards()
MagicianGuessesCard()