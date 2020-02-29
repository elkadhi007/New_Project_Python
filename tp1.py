nom = input("donner le nom de joueur : ")
age = input ("donner l' age de joueur : ")
age = int (age)
if(age<14 and age>10):
    print("le joueur " +nom+ " appartient au groupe 'minime'")
elif(age < 18):
    print("le joueur " +nom+ " appartient au groupe 'cadet'")
elif(age < 20):
    print("le joueur " +nom+ " appartient au groupe 'junuior'")
else :
    print("le joueur " +nom+ " appartient au groupe 'seniuor'")



