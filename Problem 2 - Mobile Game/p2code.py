fp = open('Problem 2 - Mobile Game/p2input.txt')
inputlist=[]
for line in fp.readlines():
    line=line.split()
    line=list(map(int, line))
    inputlist.append(line)
fp.close() 

t=int(inputlist[0][0])
inputlist=inputlist[1:]

resultslist=[]
for x in range(t): 
    line1=inputlist[2*x]
    line2=inputlist[2*x+1]
    line2.sort(reverse=True)
    n=line1[0]
    nleft=n
    a=line1[1]
    b=line1[2]
    possible=1
    while a<b and nleft>0 and possible==1: 
        if line2[-1]>a: 
            possible=0
            print(-1)
        else: 
            enemyselected=line2[0]
            es=0
            while enemyselected>=a and es<len(line2): 
                es+=1
                enemyselected=line2[es]
            if es>=len(line2): 
                print(-1)
                possible=0
            a+=enemyselected
            del line2[es]
            nleft-=1
    if possible==1 and a>=b: 
        print(n-nleft)
    elif possible==1 and nleft<=0 and a<b: 
        print(-1)
    elif possible==1:
        print(-1)