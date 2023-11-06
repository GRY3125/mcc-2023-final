n=20000 
m=8023
sumofab=[]
sumofcard=[]
absorted=[]
cardsorted=[]
fp = open('3-innovation/p3input.txt')
for line in fp.readlines():
    cardval=line.split()
    aabb=int(cardval[-4])+int(cardval[-3])
    sumofab.append(aabb)
    absorted.append(aabb)
    ccdd=int(cardval[-2])+int(cardval[-1])
    sumofcard.append(aabb+ccdd)
    cardsorted.append(aabb+ccdd)
fp.close() 

absorted.sort(reverse=True)
cardsorted.sort(reverse=True)
sum=0

pickedabs=absorted[:m-1]
indexlistpabs=[]
choosingindexab=sumofab
cardvalues=sumofcard
possiblecdsmaybe=[]
for a in range(len(pickedabs)):
    sum+=pickedabs[a]
    for b in range(sumofab.count(pickedabs[a])):
        yes=choosingindexab.index(pickedabs[a])
        indexlistpabs.append(yes)
        possiblecdsmaybe.append(int(sumofcard[yes])-int(sumofab[yes]))
        choosingindexab[yes]=0
        cardvalues[yes]=0
indexlistpabs.sort() 
cardvalues.sort(reverse=True)
possiblecdsmaybe.sort(reverse=True)

suma=0
suma+=absorted[m-1]
suma+=possiblecdsmaybe[0]


sumb=0
sumb+=cardvalues[0]

print(max((sum+suma),(sum+sumb)))