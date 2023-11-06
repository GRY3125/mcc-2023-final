sum=0
fp = open('5-rectangles/p5t4input.txt')
for line in fp.readlines():
    line=line.split()
    sum+=int(line[0])*int(line[1])
fp.close() 

print(sum)