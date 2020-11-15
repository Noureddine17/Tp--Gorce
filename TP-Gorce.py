import mysql.connector
import random


con= mysql.connector.connect(host='127.0.0.1 ',database='tp-gorce',user='root',password='')
cursor=con.cursor()

request= 'select * from user'
cursor.execute(request)
users=cursor.fetchall()

request2='select * from film '
cursor.execute(request2)
films=cursor.fetchall()

request3='select * from acteur '
cursor.execute(request3)
acteurs=cursor.fetchall()

request4='select * from jouer '
cursor.execute(request4)
jouer=cursor.fetchall()

request5='select * from realisateur '
cursor.execute(request5)
realisateurs=cursor.fetchall()


def exercice():
    a = input("Entrez votre mail : ")
    b = input("Entrez votre mdp : ")
    for elt in users:
        if a == elt[3] and b == elt[4]:
            print("Bonjour", elt[1],elt[2])


def exercice_2():
    a=str(input('entrez votre nom: ' ))
    b=str(input('entrez votre prenom: '))
    c=str(input('entrez votre mail: '))
    d=str(input('entrez votre mdp: '))
    link = "INSERT INTO user (nom,prenom,mail,mdp) VALUES (%s,%s,%s,%s)"
    rajouter = (a,b,c,d)
    print(rajouter)
    cursor.execute(link,rajouter)
    con.commit()


def exercice_3():
    film = input("entrez le nom du Film : ")
    for elt in films:
        if film in elt[1]:
            print(elt[1])


def exercice_4():
    film = input("entrez le nom du Film : ")
    for elt in films:
        if film in elt[1]:
            var = elt[5]
            for i in realisateurs:
                if var == i[0]:
                    print(elt[1],"réalisé par ",i[1],i[2])

def exercice_5():
    film = input("entrez le nom du Film : ")
    for elt in films:
        if film in elt[1]:
            var = elt[5]
            for i in realisateurs:
                if var == i[0]:
                    print(elt[1], 'réalisé par ',i[1],i[2],", ont joué dedans : ")
                    print("-----------------")
                    for a in jouer:
                        if elt[0] == a[0]:
                            for x in acteurs:
                                if a[1] == x[0]:
                                    print(x[1] ," ", x[2])



# Liste = [exercice,exercice_2,exercice_3,exercice_4,exercice_5]
# a = random.choice(Liste)
# a()