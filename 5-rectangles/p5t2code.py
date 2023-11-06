# 168r 1b
x=0
ys=[]
fp = open('5-rectangles/p5t2input.txt')
for line in fp.readlines():
    line=line.split()
    ys.append(int(line[0]))
    x+=int(line[1])
fp.close() 
ys.sort(reverse=True)
print(ys)


print(x*ys[0])