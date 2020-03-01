def tran():
    s = int(input())
    T = input()
    lis = t.split()
    Q =int(input())
    for q in range(0,Q):
        tot=0
        q = int(input("  : "))
        for t in range(0,s):
            tot +=int(lis[t])
            if(tot>=q):
                print(t)