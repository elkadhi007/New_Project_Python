import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="remindapp"
    )
mycursor=mydb.cursor()
print("connected")
class Rappel :

    def __init__(self,id,titre,date,type,description):
        self.id=id
        self.titre=titre
        self.date=date
        self.type=type
        self.description=description
    def __init__(self,titre,date,type,description):
        self.titre=titre
        self.date=date
        self.type=type
        self.description=description
    def create(self):
        sql ="INSERT INTO `rappel`( `titre`, `date`, `type`, `descripition`) VALUES (%s,%s,%s,%s)"
        val=(self.titre,self.date,self.type,self.description)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"record inserted.")
    def read(self):
        mycursor.execute("SELECT * FROM Rappel") #lire le code en bloc 
        myresult= mycursor.fetchall() #convertir en tableau 
        for x in myresult :
            print(x)


    
r1=Rappel("rdv medicale","10/02/2020","rdv","visite du medecin")
r1.read()
r2=Rappel("control medicale","14/02/2020","rdv","visite du medecin")
r1.create()
r2.create()
