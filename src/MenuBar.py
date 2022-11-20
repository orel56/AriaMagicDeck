
import tkinter as tk
from tkinter.messagebox import showerror, showwarning, askyesno # Windows that display warnings/errors messages
from tkinter.filedialog import  asksaveasfilename, askopenfilename
import popUp


def get_param(string,param):
    L=len(string)
    res=""
    if param : #we want to get the command name
        for i in range(L) : 
            if string[L-1-i]==":" :
                break
            res=string[L-1-i] + res
    else : #we want to get the label
        for item in string :
           if item==":" : 
               break
           res+=item
    return res


class MenuBar(tk.Frame) :
    def __init__ (self, app, menu) : 
        tk.Frame.__init__(self, borderwidth=1)
        self.app = app
        self.dic_menu_button={}
        self.dic_sous_menu={}
        self.variables=tk.IntVar()
        self.def_menu(menu)
        
        
    def def_menu(self,menu) :
        for item in menu :
            self.dic_menu_button[item]=tk.Menubutton (self, text = item, activebackground="#c8ad7f",activeforeground="#fff",bg="#8b6c42",fg="#fff")
            self.dic_menu_button[item].pack(side=tk.LEFT)
            sub_menu= menu[item]
            l=len(sub_menu)
            key="SousMenu"+item
            self.dic_sous_menu[key]=tk.Menu(self.dic_menu_button[item],tearoff=False)
            for i in range(l) : 
                func_name=get_param(sub_menu[i], 1)
                if func_name!="check_box" :
                    self.dic_sous_menu[key].add_command(label=get_param(sub_menu[i], 0),command=getattr(self, func_name))
                else :
                    self.dic_sous_menu[key].add_checkbutton(variable=self.variables,label=get_param(sub_menu[i], 0))
            self.dic_menu_button[item].configure(menu= self.dic_sous_menu[key])
    
    def pop_up_generate(self):
        pop_generate=popUp.PopUpGenerate(self.app,titre="Générer un nouveau jeu de cartes")
        result=pop_generate.resultat
        try :
            if result[1]!="error" and result[2]!="error":
                self.app.app_deck.generate_new_deck(nbr=result[0],to_add=result[1],to_avoid=result[2])
                self.app.update_canvas()
            else : 
                showwarning(title="Atention au nom des cartes, réessayer", message="Le nom des cartes doit être rentré en français sous le format : as/deux/trois... de ... , as/deux/trois... de ... ")
        except TypeError : 
            showwarning(title="Validation", message="La fenêtre a été fermée sans valider.")


          
    def pop_up_add_card(self):
        pop_add_card=popUp.PopUpAddCard(self.app,titre="Ajout d'une carte au jeu")
        result=pop_add_card.resultat
        try :
            if result[2]!="error":
                self.app.app_deck.add_card(from_discard=result[0], rand=result[1],card=result[2])
                self.app.update_canvas()
            else : 
                showwarning(title="Atention au nom de la carte, réessayer", message="Le nom des cartes doit être rentré en français sous le format : as/deux/trois... de ...")
        except TypeError : 
            showwarning(title="Validation", message="La fenêtre a été fermée sans valider.")