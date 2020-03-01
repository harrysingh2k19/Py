def rev(a):
    s, val, lis, re = 0, "", [ ], ""
    while(ord(a[s])>47 and ord(a[s])<58):
        val=val+a[s]
        s=s+1
    val=int(val)
    a=a[s:]
    for b in range(26):lis.append(int(b*val%26))
    for b in range(len(a)):
        if(ord(a[b])>64 and ord(a[b])<91):
            re=re+chr(lis.index(ord(b)-65)+65)
        else:
            re=re+chr(lis.index(ord(b)-97)+97)
    print(re)
    return val

a = input("input a : ")
print(rev(a))