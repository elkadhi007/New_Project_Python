x=-1
def controle(x):
    while x<2:
        x=int(input("donner un entier sup à 1 : "))
        return x
    
def parite (y):
    if (y%2==0):
        return True

a=controle(-1)
b=controle(-1)

def boucle (a,b):
    for i in range (a,b+1):
        if (parite(i)):
            print(i)



        

    

      