nombre = input ("donner un entier compose de 3 chiffre : ")
nombre = int(nombre)
centaine=nombre // 100
x = nombre % 100
dizaine = x // 10 
unitiane = x % 10 
somme = centaine + dizaine + unitiane 
if (somme%3 == 0):
    print("cette nombre " +str(nombre)+ " est diviser par 3 ")
else :
    print("cette nombre " +str(nombre)+ " n'est pas diviser par 3 ")


