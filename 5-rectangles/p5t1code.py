# 7r 3b
minsum=100
xs=[]
ys=[]
fp = open('5-rectangles/p5t1input.txt')
for line in fp.readlines():
    line=line.split()
    ys.append(int(line[0]))
    xs.append(int(line[1]))
fp.close() 

for a in range(5): 
    for b in range(a+1, 6): 
        x1=xs[0:a+1]
        x2=xs[a+1:b+1]
        x3=xs[b+1:]
        y1=ys[0:a+1]
        y2=ys[a+1:b+1]
        y3=ys[b+1:]
        y1.sort(reverse=True)
        y2.sort(reverse=True)
        y3.sort(reverse=True)
        actualy1=y1[0]
        actualy2=y2[0]
        actualy3=y3[0]
        actualx1=0
        actualx2=0
        actualx3=0
        for c in range(len(x1)): 
            actualx1+=x1[c]
        for c in range(len(x2)): 
            actualx2+=x2[c]
        for c in range(len(x3)): 
            actualx3+=x3[c]
        sum=actualx1*actualy1+actualx2*actualy2+actualx3*actualy3
        if sum<minsum: 
            minsum=sum
print(minsum)