def getDivisbleLimit(limit):
    control = 1
    v=0
    while(1):
        for i in range (1,limit):
            if control%i != 0:
                v=1
        if v==0:
            return control
        control=control+1
        v=0


print(getDivisbleLimit(20))