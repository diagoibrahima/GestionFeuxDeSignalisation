from tkinter import *
 
def route():
 can.create_rectangle(50,50,250,250,width=1,fill="black")
 
def passage_pieton():
    for i in range(8):
        can.create_rectangle(55+25*i,120,70+25*i,180,width=1,fill="white")
 
def feux(x,y,rayon,couleur):
    can.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur)
 
import time

def changefeu():

    #Premier etat___________________________________________________

    feux(30,120,10,"green")    # vue feux vert pour pieton a droite
    can.update() 

    feux(270,180,10,"green")       #vue pieton venant vers la gauche    
    can.update()

    feux(270,120,10,"red")    #vue feux vert pour es pieton a gauche
    can.update()

    feux(30,180,10,"red")       #vue voiture venant vers le bas
    can.update()
             
    
    time.sleep(3)              #CHANGEMENT DES FEUX APRES 3 SECONE
    #Deuxieme etat___________________________________________________

    feux(30,120,10,"red")    # vue feux vert pour pieton a droite
    can.update() 

    feux(270,180,10,"red")       #vue pieton venant vers la gauche    
    can.update()

    feux(270,120,10,"orange")    #vue feux vert pour es pieton a gauche
    can.update()

    feux(30,180,10,"orange")       #vue voiture venant vers le bas
    can.update()


    time.sleep(2)              #CHANGEMENT DES FEUX APRES 2 SECONE
    #Troisieme etat___________________________________________________

    feux(30,120,10,"red")    # vue feux vert pour pieton a droite
    can.update() 

    feux(270,180,10,"red")       #vue pieton venant vers la gauche    
    can.update()

    feux(270,120,10,"green")    #vue feux vert pour es pieton a gauche
    can.update()

    feux(30,180,10,"green")       #vue voiture venant vers le bas
    can.update()



 
fen = Tk()
fen.title("Feux Rouges")
 
 
can = Canvas(fen, bg ="light grey", width =500, height =500)
can.grid(row =0, column =0)
route()
passage_pieton()
a=1
changefeu()
Button(fen,text='Changer',command=changefeu).grid(row =1, column =0,sticky=W)
Button(fen,text='Quitter',command=fen.destroy).grid(row =1, column =0,sticky=E)
 
fen.mainloop()