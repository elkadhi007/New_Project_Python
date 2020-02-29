c=1
while c :
    a= input ("donner un entier a : ")
    b = input ("donner un entier b : ")
    a=int(a)
    b=int(b)
    while not (a*b==0):
        if a>b :
            r=a-b
            a=r
        else :
            r=b-a
            b=r
    if a==0:
        print ("PGCD = "+str(b))
    else :
        print ("PGCD = "+str(a))
    choix=input("voulez vous continue Y/N: ")
    if choix=="Y":
        c=1
    else:
        c=0    
