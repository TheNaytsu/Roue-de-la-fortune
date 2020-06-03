from random import randint

Listemots=[["le mont fuji","montagne"],["le mont olympe","montagne"],["chili con carne","plat"],["pirate des caraibes","film"],["le roi lion","film"],["le mexique","pays"],["le mozambique","pays"],["au clair de la lune","chanson"],["petit papa noel","chanson"],["carpe diem","expression"],["avoir une faim de loup","expression"],["le squash","sport"],["haltérophilie","sport"],["jacques brel","celebrite"],["jean reno","celebrite"]]
Listeconsonne =["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
Listevoyelle = ["a", "e", "i", "o", "u", "y"]
Roue=["Banqueroute",400,350,200,100,150,200,100,200,500,"Banqueroute",150,200,150,"Passe",400,250,100,0,150,250,350,150,250]
RoueFinale=[20000,5000,10000,7500,5000,10000,20000,5000,25000,7500,10000,5000,7500,100000,5000,15000,7500,25000,5000,7500,15000,5000,7500,10000]
class Joueur:
    def __init__(self,nom):
        self.nom = nom
        self.argent = 0
        self.argentremporte = 0


def trouvermots(Listemots):
    rand = randint(0,len(Listemots)-1)
    return Listemots[rand].pop(1),Listemots[rand].pop(0),rand


def tournerroue(Roue):
    rand = randint(0,len(Roue)-1)
    return Roue[rand]


def testelettre(poslettre,motaffichage,cpt):
    postrouve = 0
    for k in range(len(poslettre)):
        if cpt == int(poslettre[k]):
            print(motaffichage[cpt],end="")
            postrouve +=1
    if postrouve == 0:
        return False

def affichermot(motaffichage,poslettre):
    cpt = 0
    for i in range(len(motaffichage)):
        if len(poslettre) != 0:
            if motaffichage[cpt] == " ":
                print(" ",end="")
                cpt += 1
            elif testelettre(poslettre,motaffichage,cpt) == False:
                print("_", end="")
                cpt += 1
            else:
                cpt += 1
        else:
            if  motaffichage[cpt] == " ":
                print(" ", end="")
                cpt += 1
            else:
                print("_",end="")
                cpt += 1
    print(end="\n")

def testerconsonne(Listeconsonne,lettre):
    for i in range(len(Listeconsonne)):
        if lettre == Listeconsonne[i]:
            return True
    return False

def consonnevalide(Listeconsonne,Lettrejoueur,Lettredonnées):
    choix = input("Quel est votre consonne? ")
    if not testerconsonne(Listeconsonne,choix):
        print("Ce n'est pas une consonne valide")
        return False
    for i in range(len(Lettrejoueur)):
        if choix == Lettrejoueur[i]:
            print("Ce n'est pas une consonne valide")
            return False
    for j in range(len(Lettredonnées)):
        if choix == Lettredonnées[j]:
            print("Ce n'est pas une consonne valide")
            return False
    return choix

def voyellevalide(Listevoyelle,Lettrejoueur,Lettredonnées):
    choix = input("Quel est votre voyelle? ")
    if not testervoyelle(Listevoyelle,choix):
        print("Ce n'est pas une voyelle valide")
        return False
    for i in range(len(Lettrejoueur)):
        if choix == Lettrejoueur[i]:
            print("Ce n'est pas une voyelle valide")
            return False
    for j in range(len(Lettredonnées)):
        if choix == Lettredonnées[j]:
            print("Ce n'est pas une voyelle valide")
            return False
    return choix

def testervoyelle(Listevoyelle,lettre):
    for i in range(len(Listevoyelle)):
        if lettre == Listevoyelle[i]:
            return True
    return False

def gagnantFinal(Joueurs):
    gagnant = Joueurs[0]
    for i in range(len(Joueurs)):
        if gagnant.argentremporte < Joueurs[i].argentremporte:
            gagnant = Joueurs[i]
    return gagnant

def Partie(Roue,Listemots,Listevoyelle,Listeconsonne):
    Joueur1 = Joueur(1)
    Joueur2 = Joueur(2)
    Joueur3 = Joueur(3)
    Joueur1.nom = input("Quel est le nom du premier joueur? ")
    Joueur2.nom = input("Quel est le nom du deuxième joueur? ")
    Joueur3.nom = input("Quel est le nom du troisième joueur? ")
    Joueurs = [Joueur1,Joueur2,Joueur3]
    rand = 0
    theme,mot,rand = trouvermots(Listemots)
    del(Listemots[rand])
    Manche(Roue,mot,theme,Joueurs,Listevoyelle,Listeconsonne)
    print("Début de la 2ème manche.")
    theme,mot,rand = trouvermots(Listemots)
    del(Listemots[rand])
    Manche(Roue, mot,theme, Joueurs,Listevoyelle,Listeconsonne)
    print("Début de la 3ème manche.")
    theme,mot,rand = trouvermots(Listemots)
    del(Listemots[rand])
    Manche(Roue, mot,theme, Joueurs,Listevoyelle,Listeconsonne)
    print("Début de la dernière manche.")
    theme,mot,rand = trouvermots(Listemots)
    del(Listemots[rand])
    Manche(Roue, mot,theme, Joueurs,Listevoyelle,Listeconsonne)
    gagnant = gagnantFinal(Joueurs)
    print("Le qualifié pour la finale est",gagnant.nom,"avec la somme de",gagnant.argentremporte,"€")
    print("Début de la Manche finale.")
    theme,mot,rand = trouvermots(Listemots)
    del(Listemots[rand])
    mancheFinale(RoueFinale,mot,theme,Listevoyelle,Listeconsonne,gagnant)


def Manche(Roue,mot,theme,Joueurs,Listevoyelle,Listeconsonne):
    motaffichage = mot
    poslettre = []
    lettresup = ""
    lettresuptab= []
    posJoueur = 0
    while len(mot) !=0:
        for i in range(len(Joueurs)):
            print("L'argent de", Joueurs[i].nom, "est", Joueurs[i].argent)
        print("Le mot est : ", end="")
        affichermot(motaffichage, poslettre)
        print("Le thème est :",theme)
        print("C'est au joueur", Joueurs[posJoueur].nom, "de jouer.")
        if(Joueurs[posJoueur].argent >= 200):
            reponse = input("Voulez vous achetez une voyelle pour 200€ ? Oui ou Non : ")
            if reponse == "oui" or reponse == "Oui":
                    voyelle = input("Entrez la voyelle que vous voulez acheter : ")
                    if not testervoyelle(Listevoyelle, voyelle):
                        print("Dommage ce n'est pas une voyelle. Vous passez donc votre tour.\n")
                        posJoueur += 1
                        if posJoueur == 3:
                            posJoueur = 0
                    else:
                        cpt = 0
                        for i in range(len(mot)):
                            for j in range(len(lettresuptab)):
                                if lettresuptab[j] == voyelle:
                                    voyelle = ""
                            if voyelle == mot[i]:
                                cpt = cpt + 1;
                                lettresup = voyelle
                        Joueurs[posJoueur].argent -= 200
                        for p in range(len(motaffichage)):
                            if (voyelle == motaffichage[p]):
                                poslettre.append(p)
                        if lettresup != "":
                            lettresuptab.append(lettresup)
                            mot = mot.replace(lettresup, "")
                            lettresup = ""
                        if cpt == 0 and voyelle == "":
                            print("Dommage cette lettre a déjà était utilisé. Vous passez donc votre tour.\n")
                            posJoueur += 1
                            if posJoueur == 3:
                                posJoueur = 0
                        elif cpt == 0:
                            print("Dommage ce n'est pas une voyelle présente. Vous passez donc votre tour.\n")
                            posJoueur += 1
                            if posJoueur == 3:
                                posJoueur = 0
                        else:
                            print("Bravo ! Elle y était.\n")
            elif reponse == "Non" or reponse == "non":
                print("D'accord.")
            else:
                if (reponse != "Non" and reponse != "non"):
                    print("Votre réponse n'était ni non ni oui donc elle est compté comme un refus")
        print("Tournez la roue.")
        argent = tournerroue(Roue)
        if argent == "Banqueroute":
            print('La roue est tombé sur', argent,"donc vous perdez tout vos gains ainsi que la main.\n")
            Joueurs[posJoueur].argent =0
            posJoueur += 1
            if posJoueur == 3:
                posJoueur = 0
        elif argent == "Passe":
            print('La roue est tombé sur', argent, "donc vous perdez la main.\n")
            posJoueur += 1
            if posJoueur == 3:
                posJoueur = 0
        else:
            print('La roue est tombé sur', argent,"€")
            choix = input("Que décidez-vous de faire ? Ecrivez 'Consonne' ou donnnez la réponse : ")
            if choix == "consonne" or choix == "Consonne":
                lettre = input("Entrez la consonne de votre choix : ")
                if not testerconsonne(Listeconsonne, lettre):
                    print("Dommage ce n'est pas une consonne. Vous passez donc votre tour.\n")
                    posJoueur += 1
                    if posJoueur == 3:
                        posJoueur = 0
                else:
                    cpt = 0
                    for i in range(len(mot)):
                        for j in range(len(lettresuptab)):
                            if lettresuptab[j] == lettre:
                                lettre = ""
                        if lettre == mot[i]:
                            Joueurs[posJoueur].argent += argent
                            cpt = cpt + 1;
                            lettresup = lettre
                    for p in range(len(motaffichage)):
                        if (lettre == motaffichage[p]):
                            poslettre.append(p)
                    if lettresup != "":
                        lettresuptab.append(lettresup)
                        mot = mot.replace(lettresup, "")
                        lettresup = ""
                    if cpt == 0 and lettre == "":
                        print("Dommage cette lettre a déjà était utilisé. Vous passez donc votre tour.\n")
                        posJoueur += 1
                        if posJoueur == 3:
                            posJoueur = 0
                    elif cpt == 0:
                        print("Dommage ce n'est pas une consonne présente. Vous passez donc votre tour.\n")
                        posJoueur += 1
                        if posJoueur == 3:
                            posJoueur = 0
                    else:
                        print("Bravo vous avez gagné", cpt * argent, "€ et vous pouvez rejouer.\n")
            elif choix == "réponse" or choix == "Réponse" or choix == "Reponse" or choix == "reponse":
                mot = input("Entrez le mot de votre choix : ")
                if mot == motaffichage:
                    poslettre = []
                    for i in range(len(motaffichage)):
                        poslettre.append(i)
                    Joueurs[posJoueur].argent += argent
                    mot = ""
                    print("Bravo vous avez trouvé. Vous avez gagné\n")
                else:
                    print("Dommage ce n'est pas ce mot. Vous passez donc votre tour\n")
                    posJoueur += 1
                    if posJoueur == 3:
                        posJoueur = 0
            elif choix == motaffichage:
                poslettre = []
                for i in range(len(motaffichage)):
                    poslettre.append(i)
                Joueurs[posJoueur].argent += argent
                mot = ""
                print("Bravo vous avez trouvé. Vous avez gagné\n")
            else:
                print("Ceci n'est pas une réponse valable, vous passez votre tour. Veuillez écrire Réponse ou Consonne la prochaine fois.\n")
                posJoueur += 1
                if posJoueur == 3:
                    posJoueur = 0
    print("Le mot final était :",motaffichage)
    print("Le gagnant est",Joueurs[posJoueur].nom,"et il gagne",Joueurs[posJoueur].argent,"€")
    Joueurs[posJoueur].argentremporte = Joueurs[posJoueur].argent + Joueurs[posJoueur].argentremporte
    for i in range(len(Joueurs)):
        Joueurs[i].argent = 0
    print("La manche est finie\n")

def mancheFinale(RoueFinale,mot,theme,Listevoyelle,Listeconsonne,gagnant):
    Lettredonnées = ["r","s","t","l","n","e"]
    Lettrejoueur = []
    motaffichage = mot
    poslettre = []
    lettresup = ""
    lettresuptab= []
    print('5 consonnes vous sont données : "R,S,T,L,N" et 1 voyelle : "E". Vous devez proposer 3 consonnes et une voyelle puis vous devez donner votre réponse')
    print("Le mot est : ", end="")
    cpt = 0
    argent = tournerroue(RoueFinale)
    for l in range(len(Lettredonnées)):
        for i in range(len(mot)):
            for j in range(len(lettresuptab)):
                if lettresuptab[j] == Lettredonnées[l]:
                    Lettredonnées[l] = ""
            if Lettredonnées[l] == mot[i]:
                cpt = cpt + 1;
                lettresup = Lettredonnées[l]
        for p in range(len(motaffichage)):
            if (Lettredonnées[l] == motaffichage[p]):
                poslettre.append(p)
        if lettresup != "":
            lettresuptab.append(lettresup)
            mot = mot.replace(lettresup, "")
            lettresup = ""
    affichermot(motaffichage, poslettre)
    print("Le thème est :",theme)
    while len(Lettrejoueur) <3:
        choix = consonnevalide(Listeconsonne, Lettrejoueur, Lettredonnées)
        while choix == False:
             choix = consonnevalide(Listeconsonne, Lettrejoueur, Lettredonnées)
        Lettrejoueur.append(choix)
        print(Lettrejoueur)
    choix = voyellevalide(Listevoyelle, Lettrejoueur, Lettredonnées)
    while choix == False:
        choix = voyellevalide(Listevoyelle, Lettrejoueur, Lettredonnées)
    Lettrejoueur.append(choix)
    cpt = 0
    for l in range(len(Lettrejoueur)):
        for i in range(len(mot)):
            for j in range(len(lettresuptab)):
                if lettresuptab[j] == Lettrejoueur[l]:
                    Lettrejoueur[l] = ""
            if Lettrejoueur[l] == mot[i]:
                cpt = cpt + 1;
                lettresup = Lettrejoueur[l]
        for p in range(len(motaffichage)):
            if (Lettrejoueur[l] == motaffichage[p]):
                poslettre.append(p)
        if lettresup != "":
            lettresuptab.append(lettresup)
            mot = mot.replace(lettresup, "")
            lettresup = ""
    print(Lettrejoueur)
    affichermot(motaffichage, poslettre)
    choixfinale = input("Quel est votre réponse? ")
    if choixfinale == motaffichage:
        print("Bravo vous repartez avec le contenu de l'enveloppe qui était",argent,"€")
        gagnant.argentremporte += argent
        print("Ce qui fait que vous avez gagné un total de",gagnant.argentremporte,"€")
    else:
        print("Désolé vous avez perdu le mot était,",motaffichage,"et dans l'enveloppe il y avait",argent)




Partie(Roue,Listemots,Listevoyelle,Listeconsonne)

