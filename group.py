def group():
    t=int(input())
    test=1
    final=0
    while(test<=t):
        first = input()
        firs =first.split()
        N=int(firs[0])
        K=int(firs[1])
        for a in firs:
            print(a)
        tot = 0
        i=1
        temp=N
        while(N>K):
            tot += int(( (temp-K*i)-1) /2 )
            i+=1 
            N-=K
            print("tot=",tot, "N = ",N,"K = ",K)
        if (t==test):
            final=tot
        else: 
            print(tot) 
        test+=1
    return final

print(group())