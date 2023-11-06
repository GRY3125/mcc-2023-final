n=18
k=2
xinput=input()
xinput=xinput.split()
listofsubsets=[0]

for y in range(n): 
    listofsubsets.extend(listofsubsets)
    for d in range(len(listofsubsets)//2): 
        listofsubsets[d]+=int(xinput[y])
        listofsubsets[d]=listofsubsets[d]%998244353
sum=0
for f in range(len(listofsubsets)): 
    sum+=(listofsubsets[f]**k)%998244353
print(sum%998244353)