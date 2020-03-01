def persistence(n):
    t=1
    a=list(str(n))
    print(a)
    for i in range(len(str(n))):
        t*=a[i]
    if t>10:persistence(t)
    else: return t        

print(persistence(999))