n=100000  
w=31337
fp = open('4-tichu/p4input.txt')
for line in fp.readlines():
    x=line
fp.close() 
x=x.split()
x=set(x)
x=list(x)
for a in range(len(x)):
    x[a]=int(x[a])
x.sort()

run=[]
breakk=[]
runnn=1
for a in range(len(x)-1): 
    if x[a]+1==x[a+1]: 
        runnn+=1
    else: 
        run.append(runnn)
        breakk.append(x[a+1]-x[a]-1)
        runnn=1
if x[-1]-1==x[-2]: 
    run[-1]+=1
else: 
    run.append(1)

maxcount=0
for a in range(len(breakk)):
    tempbreak=breakk[:]
    breaksleft=w
    count=0
    listfin=0
    count+=run[a]
    while breaksleft>=tempbreak[a] and listfin==0:
        breaksleft-=tempbreak[a]
        count+=tempbreak[a]
        tempbreak[a]=0
        if a<len(tempbreak)-1:
            a+=1
            count+=run[a]
        else:
            listfin=1
    count+=breaksleft
    if count>maxcount: 
        maxcount=count
print(maxcount)