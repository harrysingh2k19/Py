def fun():
    val = input()
    val=val.split()
    n1= int(val[0])
    n2= int(val[1])
    if(n1<n2):lwr=n1
    else:lwr=n2
    print(lwr)
    tot=1
    if (n1%2!=0 or n2%2!=0):
        n=3
        while(n<=lwr):
            print("n =",n)
            if(n1%n==0 and n2%n==0):
                tot+=1
            n+=2
    else:
        n=2
        while(n<=lwr):
            print("n =",n)
            if(n1%n==0 and n2%n==0):
                tot+=1
            n+=2
    return tot

print(fun())