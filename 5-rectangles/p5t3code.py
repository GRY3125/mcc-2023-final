# 193r 2b
minsum=10**12
xs=[]
ys=[]
fp = open('5-rectangles/p5t3input.txt')
for line in fp.readlines():
    line=line.split()
    ys.append(int(line[0]))
    xs.append(int(line[1]))
fp.close() 

for a in range(192): 
    subx1=xs[:(a+1)]
    subx2=xs[(a+1):]
    sumx1=0
    sumx2=0
    for b in range(len(subx1)): 
        sumx1+=subx1[b]
    for b in range(len(subx2)): 
        sumx2+=subx2[b]
    suby1=ys[:(a+1)]
    suby2=ys[(a+1):]
    suby1.sort(reverse=True)
    suby2.sort(reverse=True)
    y1=suby1[0]
    y2=suby2[0]
    summm=sumx1*y1+sumx2*y2
    if summm<minsum: 
        minsum=summm
    print(summm, sumx1, sumx2, y1, y2)
print(minsum)