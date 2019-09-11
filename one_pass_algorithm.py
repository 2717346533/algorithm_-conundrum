cap = ['F','F','B','B','B','F',
        'B','B','B','F','F','B','F'
        ]

def pleaseConformOnepass(cap):
    cap = cap + [cap[0]]
    for i in range(1,len(cap)):
        if cap[i] != cap[i - 1]:
            if cap[i] != cap[0]:
                print('People in position',i,end = '')
            else:
                print('through',i - 1,'flip your caps!')

pleaseConformOnepass(cap)