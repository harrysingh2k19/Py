def kalra():
    first="4 4"
    second = "2 1 3 4"
    third = "3 4 2 1"
    st = first#input()
    stN=second#input()
    lstN = stN.split()
    n=0
    for mm in lstN:
        lstN[n] = int(mm)
        n+=1
    stM=third#input()
    lstM = stM.split()
    n=0
    for mm in lstM:
        lstM[n] = int(mm)
        n+=1
    n=0
    print (lstN)
    print (lstM)
    while (1):    
        print (lstN)
        print (lstM)
        n+=1
        st = input()
        inp = st.split()
        if(inp[0]=='R'):
            temp = lstN[-int(inp[1])]
            lstN[-int(inp[1])]=lstN[0]
            lstN[0]=temp
            if(lstN == lstM):
                break
        elif(inp[0]=='L'):
            temp = lstN[int(inp[1])-1]
            lstN[int(inp[1])-1]=lstN[-1]
            lstN[-1]=temp
            if(lstN == lstM):
                return n

print( kalra() )