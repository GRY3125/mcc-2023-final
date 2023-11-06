n=733
k=559

fp = open("Problem 1 - Collatz/p1input.txt")
for line in fp.readlines():
    nlist=line
fp.close() 

nlist=nlist.split()
sum=0
for x in range(n):
    nlist[x]=int(nlist[x])
    for y in range(k): 
        if nlist[x]%2==0: 
            nlist[x]=nlist[x]/2
        else: 
            nlist[x]=3*(nlist[x])+1
    sum+=nlist[x]
print(sum)