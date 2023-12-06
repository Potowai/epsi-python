#réalise un morpion en python   
# Date: 10/10/2018

# Importation des modules


from tkinter import *
from tkinter.messagebox import *
from random import randint

# Définition des fonctions
    
def jouer():
    global tour, joueur, symbole, cases, fini
    fini = False
    tour = 0
    joueur = randint(1,2)
    symbole = "X"
    cases = [0,0,0,0,0,0,0,0,0]
    canvas.delete("all")
    canvas.create_line(100,0,100,300, fill="black", width=3)
    canvas.create_line(200,0,200,300, fill="black", width=3)
    canvas.create_line(0,100,300,100, fill="black", width=3)
    canvas.create_line(0,200,300,200, fill="black", width=3)
    if joueur == 2:
        ia()
    else:
        canvas.bind("<Button-1>", clic)

def clic(event):
    global tour, joueur, symbole, cases, fini
    if fini == False:
        if event.x < 100:
            colonne = 0
        elif event.x < 200:
            colonne = 1
        else:
            colonne = 2
        if event.y < 100:
            ligne = 0
        elif event.y < 200:
            ligne = 1
        else:
            ligne = 2
        #print("Ligne : "+str(ligne)+" Colonne : "+str(colonne))
        #Si la case est vide alors on peut jouer
        if cases[ligne*3+colonne] == 0:
            cases[ligne*3+colonne] = joueur
            if joueur == 1:
                canvas.create_line(colonne*100+10,ligne*100+10,colonne*100+90,ligne*100+90, fill="red", width=3)
                canvas.create_line(colonne*100+90,ligne*100+10,colonne*100+10,ligne*100+90, fill="red", width=3)
                print(cases)
                joueur = 2
                symbole = "O"
            else:
                canvas.create_oval(colonne*100+10,ligne*100+10,colonne*100+90,ligne*100+90, outline="blue", width=3)
                joueur = 1
                symbole = "X"
            tour = tour + 1
            if tour > 4:
                verif()
            if fini == False:
                ia()

def ia():
    global tour, joueur, symbole, cases, fini
    if fini == False:
        if tour == 0:
            ligne = randint(0,2)
            colonne = randint(0,2)
        #Si l'IA peut gagner alors elle gagne !
        #Si l'IA ne peut pas gagner alors elle bloque !
        #Si l'IA ne peut pas bloquer alors elle joue un coin !
        #Si l'IA ne peut pas jouer un coin alors elle joue un côté !
        else:
            ligne, colonne = ia_gagne()
            if ligne == -1:
                ligne, colonne = ia_bloque()
                if ligne == -1:
                    ligne, colonne = ia_coin()
                    if ligne == -1:
                        ligne, colonne = ia_cote()
        if cases[ligne*3+colonne] == 0:
            cases[ligne*3+colonne] = joueur
            if joueur == 1:
                canvas.create_line(colonne*100+10,ligne*100+10,colonne*100+90,ligne*100+90, fill="red", width=3)
                canvas.create_line(colonne*100+90,ligne*100+10,colonne*100+10,ligne*100+90, fill="red", width=3)
                joueur = 2
                symbole = "O"
            else:
                canvas.create_oval(colonne*100+10,ligne*100+10,colonne*100+90,ligne*100+90, outline="blue", width=3)
                joueur = 1
                symbole = "X"
            tour = tour + 1
            if tour > 4:
                verif()
#Explication des fonctions de l'IA
#On vérifie si l'IA peut gagner en jouant sur une ligne, une colonne ou une diagonale et on renvoie les coordonnées de la case à jouer
def ia_gagne():
    global cases
    for i in range(3):
        if cases[i*3] == 2 and cases[i*3+1] == 2 and cases[i*3+2] == 0:
            return i,2
        elif cases[i*3] == 2 and cases[i*3+1] == 0 and cases[i*3+2] == 2:
            return i,1
        elif cases[i*3] == 0 and cases[i*3+1] == 2 and cases[i*3+2] == 2:
            return i,0
        elif cases[i] == 2 and cases[i+3] == 2 and cases[i+6] == 0:
            return 2,i
        elif cases[i] == 2 and cases[i+3] == 0 and cases[i+6] == 2:
            return 1,i
        elif cases[i] == 0 and cases[i+3] == 2 and cases[i+6] == 2:
            return 0,i
    if cases[0] == 2 and cases[4] == 2 and cases[8] == 0:
        return 2,2
    elif cases[0] == 2 and cases[4] == 0 and cases[8] == 2:
        return 1,1
    elif cases[0] == 0 and cases[4] == 2 and cases[8] == 2:
        return 0,0
    elif cases[2] == 2 and cases[4] == 2 and cases[6] == 0:
        return 2,0
    elif cases[2] == 2 and cases[4] == 0 and cases[6] == 2:
        return 1,1
    elif cases[2] == 0 and cases[4] == 2 and cases[6] == 2:
        return 0,2
    else:
        return -1,-1

def ia_bloque():
    global cases
    for i in range(3):
        if cases[i*3] == 1 and cases[i*3+1] == 1 and cases[i*3+2] == 0:
            return i,2
        elif cases[i*3] == 1 and cases[i*3+1] == 0 and cases[i*3+2] == 1:
            return i,1
        elif cases[i*3] == 0 and cases[i*3+1] == 1 and cases[i*3+2] == 1:
            return i,0
        elif cases[i] == 1 and cases[i+3] == 1 and cases[i+6] == 0:
            return 2,i
        elif cases[i] == 1 and cases[i+3] == 0 and cases[i+6] == 1:
            return 1,i
        elif cases[i] == 0 and cases[i+3] == 1 and cases[i+6] == 1:
            return 0,i
    if cases[0] == 1 and cases[4] == 1 and cases[8] == 0:
        return 2,2
    elif cases[0] == 1 and cases[4] == 0 and cases[8] == 1:
        return 1,1
    elif cases[0] == 0 and cases[4] == 1 and cases[8] == 1:
        return 0,0
    elif cases[2] == 1 and cases[4] == 1 and cases[6] == 0:
        return 2,0
    elif cases[2] == 1 and cases[4] == 0 and cases[6] == 1:
        return 1,1
    elif cases[2] == 0 and cases[4] == 1 and cases[6] == 1:
        return 0,2
    else:
        return -1,-1

def ia_coin():
    global cases
    if cases[0] == 0:
        return 0,0
    elif cases[2] == 0:
        return 0,2
    elif cases[6] == 0:
        return 2,0
    elif cases[8] == 0:
        return 2,2
    else:
        return -1,-1

def ia_cote():
    global cases
    if cases[1] == 0:
        return 0,1
    elif cases[3] == 0:
        return 1,0
    elif cases[5] == 0:
        return 1,2
    elif cases[7] == 0:
        return 2,1
    else:
        return -1,-1

def verif():
    global cases, fini
    for i in range(3):
        if cases[i*3] == cases[i*3+1] and cases[i*3] == cases[i*3+2] and cases[i*3] != 0:
            fini = True
            canvas.create_line(0,i*100+50,300,i*100+50, fill="green", width=5)
            showinfo("Fin de partie","Le joueur "+str(cases[i*3])+" a gagné !")
        elif cases[i] == cases[i+3] and cases[i] == cases[i+6] and cases[i] != 0:
            fini = True
            canvas.create_line(i*100+50,0,i*100+50,300, fill="green", width=5)
            showinfo("Fin de partie","Le joueur "+str(cases[i])+" a gagné !")
    if cases[0] == cases[4] and cases[0] == cases[8] and cases[0] != 0:
        fini = True
        canvas.create_line(50,50,250,250, fill="green", width=5)
        showinfo("Fin de partie","Le joueur "+str(cases[0])+" a gagné !")
    elif cases[2] == cases[4] and cases[2] == cases[6] and cases[2] != 0:
        fini = True
        canvas.create_line(250,50,50,250, fill="green", width=5)
        showinfo("Fin de partie","Le joueur "+str(cases[2])+" a gagné !")
    elif tour == 9:
        fini = True
        showinfo("Fin de partie","Match nul !")

# Programme principal

fenetre = Tk()
fenetre.title("Morpion")
canvas = Canvas(fenetre, width=300, height=300, bg="white")
canvas.pack()
jouer()
bouton = Button(fenetre, text="Rejouer", command=jouer)
bouton.pack()
fenetre.mainloop()



