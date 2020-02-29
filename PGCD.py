def pgcd (a,b):
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


x= int(input ("donner un entier x : "))
y= int(input ("donner un entier y : "))
pgcd(x,y)
