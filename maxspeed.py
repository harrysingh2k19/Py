def speed():
    maxd=0
    maxb=0
    checkpoint = int(input())
    dom =input()
    for a in range(2,checkpoint*2-1,2):
        if(  int(int(dom[a])-int(dom[a-2])) >maxd) :
            maxd=int(dom[a])-int(dom[a-2])
    bri = input()
    for a in range(2,checkpoint*2-1,2):
        if(  int(int(bri[a])-int(bri[a-2]) )>maxb) :
            maxb=int(bri[a])-int(bri[a-2])
    if(maxb>maxd):
        print("Brian")
        max=maxb
    elif(maxd>maxb):
        print("Dom")
        max=maxd
    else:
        print("tie")
        max=maxb
    return int(max)
print(speed())
