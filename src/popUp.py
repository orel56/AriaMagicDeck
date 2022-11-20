# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:11:02 2021
@author: Aurelian
"""

import tkinter as tk
from tkinter.messagebox import showerror, showwarning
import config as conf

class PopUp(tk.Toplevel):
    resultat=None
    def __init__ (self, conteneur, titre=" ",offx=460,offy=280) :
        tk.Toplevel.__init__(self, conteneur)
        self.labels=[]   
        self.var_valider=0
        self.protocol("WM_DELETE_WINDOW", self.terminer)
        self.title(titre)
        # title() est hérité de Toplevel
        # le dialogue apparaît au dessus de son conteneur
        self.transient(conteneur)
        #rend la fenêtre non étirable
        self.resizable(0,0)
        # détourne tous les événements vers la fenêtre de dialogue
        self.grab_set()
        # afficher la fenêtre d'aide par rapport au conteneur
        self.geometry ("+"+str(conteneur.winfo_rootx()+offx)+\
                       "+"+str(conteneur.winfo_rooty()+offy))
        self.frameContenu = tk.Frame (self, border=2, relief=tk.GROOVE)
        # définition d'un contenu du cadre frameContenu
        self.habillage()
        self.frameContenu.pack()
        # bouton d'effacement
        self.bouton_valider = tk.Button (self, text = "Valider", width = 12,\
        command = self.valider,state="disabled")
        self.bouton_valider.pack(pady=5)
        # porter le focus sur la fenêtre d'appel
        self.focus_set ()
        # boucle locale de la fenêtre
        self.wait_window (self)

    def habillage (self) :
        pass

    def valider (self, evenement = None) :
        # effacement avant de supprimer (pour le rendu)
        self.withdraw ()
        # nécessaire si dans apply() on utilise des éléments
        # qui doivent être visibles pour fournir des données
        self.update_idletasks()
        self.apply()
        
    def terminer(self, evenement=None):
        self.master.focus_set()
        self.destroy()
    def apply(self):
        pass

class PopUpAddCard(PopUp) :
    def __init__(self, conteneur,titre=" ", offx=460, offy=280):
        self.check_box=[]
        self.VarCheck=[]
        super().__init__(conteneur,titre, offx, offy)

    def habillage(self):
        self.def_labels()
        self.def_entrys()
        self.def_checkbox()
        
    def def_entrys(self):
        self.entry_var= tk.StringVar()
        self.entry=tk.Entry(self.frameContenu, textvariable=self.entry_var,state="normal", validate="key",validatecommand=(self.register(self.activ_valider),'%P','%s','%S'),invalidcommand=(self.register(self.not_valid),"%d",'%P'))
        self.entry.grid(row=2,column=1,sticky='w')

        
    def def_labels(self):
        self.labels.append(tk.Label(self.frameContenu,text="Nom de la carte à ajouter:"))
        self.labels[0].grid(row=2,column=0,sticky='w')
        self.labels.append(tk.Label(self.frameContenu,text="Depuis la défausse ? "))
        self.labels[1].grid(row=0,column=0,sticky='w')
        self.labels.append(tk.Label(self.frameContenu,text="Carte aléatoire ? "))
        self.labels[2].grid(row=1,column=0,sticky='w')
    
    def def_checkbox(self):
        self.VarCheck.append(tk.IntVar())
        self.check_box.append(tk.Checkbutton(self.frameContenu,anchor="w",command=self.activ_button,variable=self.VarCheck[0]))
        self.check_box[0].grid(row=0,column=1,sticky="w")
        self.VarCheck.append(tk.IntVar())
        self.check_box.append(tk.Checkbutton(self.frameContenu,anchor="w",command=self.activ_button,variable=self.VarCheck[1]))
        self.check_box[1].grid(row=1,column=1,sticky="w")

    def apply(self) :
        self.resultat=[self.VarCheck[0].get(),self.VarCheck[1].get(),self.entry_var.get()]
        if self.resultat[2]!="":
            self.resultat[2]=self.resultat[2].lower()
            if self.resultat[2] in conf.equivalence :
                self.resultat[2] = conf.equivalence[self.resultat[2]]
            else : 
                self.resultat[2]="error"
        self.terminer()
    
    def activ_valider(self,texte,texte_bef,texte_add) :
        not_valid_carac="<>:\"/\\|?*._-"
        if texte_add in not_valid_carac : 
            return False
        else :
            if(len(texte)==0 and texte_bef!=texte) :
               self.bouton_valider["state"]="disabled"
            elif(len(texte)==1 and texte_bef=="") : 
               self.bouton_valider["state"]="normal"
            return True

    def not_valid(self,activ,texte) : 
        if activ=="1":
            self.entry.delete(first=len(texte)-1,last=len(texte))

    def activ_button(self):
        if self.VarCheck[0].get() or self.VarCheck[1].get():
           self.bouton_valider["state"]="normal"
        else : 
           self.bouton_valider["state"]="disabled"


class PopUpGenerate(PopUp) :
    def __init__(self, conteneur, titre=" ", offx=460, offy=280):
        self.entrys=[]
        self.entry_var=[]
        super().__init__(conteneur,titre, offx, offy)

    def habillage(self):
        self.def_labels()
        self.def_entrys()
        
    def def_entrys(self):
        self.entry_var.append(tk.StringVar())
        self.entrys.append(tk.Entry(self.frameContenu, textvariable=self.entry_var[0],state="normal", validate="key",validatecommand=(self.register(self.activ_valider),'%P','%s','%S','%W'),invalidcommand=(self.register(self.not_valid),"%d",'%P','%W')))
        self.entrys[0].grid(row=0,column=1,sticky='w')

        self.entry_var.append(tk.StringVar())
        self.entrys.append(tk.Entry(self.frameContenu, textvariable=self.entry_var[1],state="normal", validate="key",validatecommand=(self.register(self.activ_valider),'%P','%s','%S','%W'),invalidcommand=(self.register(self.not_valid),"%d",'%P','%W')))
        self.entrys[1].grid(row=1,column=1,sticky='w')


        self.entry_var.append(tk.StringVar())
        self.entrys.append(tk.Entry(self.frameContenu, textvariable=self.entry_var[2],state="normal", validate="key",validatecommand=(self.register(self.activ_valider),'%P','%s','%S','%W'),invalidcommand=(self.register(self.not_valid),"%d",'%P','%W')))
        self.entrys[2].grid(row=2,column=1,sticky='w')

        
    def def_labels(self):
        self.labels.append(tk.Label(self.frameContenu,text="Nombre de carte du jeu :"))
        self.labels[0].grid(row=0,column=0,sticky='w')
        self.labels.append(tk.Label(self.frameContenu,text="Liste des cartes à ajouter au jeu :"))
        self.labels[1].grid(row=1,column=0,sticky='w')
        self.labels.append(tk.Label(self.frameContenu,text="Liste des cartes à ne pas ajouter au jeu :"))
        self.labels[2].grid(row=2,column=0,sticky='w')

    def apply(self) :
        self.resultat=[self.entry_var[0].get(),self.entry_var[1].get(),self.entry_var[2].get()]

        try : 
           self.resultat[0]=int(self.resultat[0])
           self.resultat[1]=extract_card_names(self.resultat[1])
           self.resultat[2]=extract_card_names(self.resultat[2]) 
        except ValueError:
           self.resultat[1]="error"
        
        self.terminer()    
        
    def activ_valider(self,texte,texte_bef,texte_add,name) :
        entry_id=name[-1]
        if entry_id=='y':
            try: 
                if int(texte)<=52 and 0<=int(texte) :
                    self.bouton_valider["state"]="normal"
                else:
                    return False 
                
                return True
            except ValueError:
                if texte=="":
                    self.bouton_valider["state"]="disabled"
                    return True
                else :
                    return False
        else :
            not_valid_carac="<>:\"/\\|?*._-"
            if texte_add in not_valid_carac : 
                return False
            else :
                return True

    def not_valid(self,activ,texte,name) : 
        entry_id=name[-1]
        if activ=="1":
            try :
                self.entrys[int(entry_id)-1].delete(first=len(texte)-1,last=len(texte))
            except ValueError :
                self.entrys[0].delete(first=len(texte)-1,last=len(texte))


def extract_card_names (cards):
    cards=cards.lower()
    res=[]
    if cards=="":
        return [[]]

    cards=cards.split(",")

    for card in cards : 
        card=card.strip()
        if card in conf.equivalence :
            res.append(conf.equivalence[card])
        else : 
            res="error"
            break
    return res


    
if __name__=="__main__" : 
    print(extract_card_names("dame de pique ,    as de trèfle    , roi de coeur"))




