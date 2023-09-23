
# Print + variable, demande du nom et de l'âge de la personne

nom_de_la_personne = input("Quel est ton nom?")

#nom_de_la_personne = "toto"
#age_de_la_personne = 30


# verification / Condition avec exception while True :
# Je vérifie si age est bien de type int pour fermer la boucle


while True:

    try :
        age_de_la_personne = int(input("Vous avez quel age?"))
        #age_prochain = int(age_de_la_personne) + 1 // Incrémentation
    except:
        print("Erreur : Vous devez rentrer un nombre pour l'âge")

    else:
        print("Je m'appelle" + " " + nom_de_la_personne + ".")
        print("J'ai " + str(age_de_la_personne) + " ans . L'année prochaine j'aurais " + str(age_de_la_personne + 1) + " ans.")
        break # Sortir de la condition si réussit

# Autre manière de traiter la condition est la boucle en maintenant la boucle si elle est == 0

"""
age_de_la_personne = 0

while age_de_la_personne == 0:

    age_de_la_personne_str = input("Vous avez quel age?")

    try :
        age_de_la_personne = int(age_de_la_personne_str)
        #age_prochain = int(age_de_la_personne) + 1
    except:
        print("Erreur : Vous devez rentrer un nombre pour l'âge")

print("Je m'appelle" + " " + nom_de_la_personne + ".")
print("J'ai " + str(age_de_la_personne) + " ans . L'année prochaine j'aurais " + str(age_de_la_personne + 1) + " ans.")
 """



#Connaître le type de donnée (type(donnee))

#print(type(nom_de_la_personne))

#convertir l'age en string
# str(age) -> "age "


""" boucle while : "tant que" ...

n = 0 # crée la variable
#n = 10 # réaffecte la variable
print (n)

 # incrémente la variable

print (n)

print("début de la boucle")

while n < 10:
    print("Valeur de n :" + str(n))
    n = n + 1

print("fin de la boucle")"""

"""mot_de_passe = ""
while not mot_de_passe == "TOTO" :
    mot_de_passe = input("Quel est le mot de passe ?")

print("Bon mot de passe")"""




