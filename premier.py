x=-1
while x<2 :
    x=int(input("donner un entier sup à 1 : "))
for i in range (2,x):
    if (x%i==0):
        break
if i<=int(x//2):
    print("n est pas premier ")
else :
    print("premier")