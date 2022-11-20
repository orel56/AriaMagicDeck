import tkinter as tk #Module with all the graphics componants 
from tkinter.messagebox import showerror, showwarning # Windows that display warnings/errors messages
from Deck import Deck
from MenuBar import MenuBar
from PIL import ImageTk,Image
import config as conf

class App(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.app_deck=Deck()
        
        self.labels=[]

        self.app_height= float(200) 
        self.app_width= float(550) 
        self.configure(bg="#e0cda9")
        self.protocol("WM_DELETE_WINDOW",self.close) # Allows to close the window with the red cross
        self.title("Jeu de carte magie d'Aria") 
        self.geometry(str(int(self.app_width))+"x"+str(int(self.app_height))) # Set the initial window's geometry 
        self.resizable(False,False)

        self.init_menu({"Fichier" : ["Générer un nouveau jeu de carte:pop_up_generate","Ajouter une carte au deck:pop_up_add_card"]})

        self.init_canvas()

        self.init_label()

        self.shuffle_button=tk.Button(self.menu_bar,text="Mélanger", command = self.app_deck.shuffle,state="normal", activebackground="#c8ad7f",activeforeground="#fff",bg="#8b6c42",fg="#fff",highlightbackground="#8b6c42",relief="flat")
        self.shuffle_button.pack(side=tk.LEFT)

    def close(self):
        self.app_deck.save_deck()
        self.quit()

    def init_label(self) :
        self.labels.append(tk.Label(text="♦ Carreaux : Manipulation de la matière",bg="#e0cda9"))
        self.labels[0].place(x=210,y=65)
        self.labels.append(tk.Label(text="♥ Cœurs : Manipulation des cœurs",bg="#e0cda9"))
        self.labels[1].place(x=210,y=85)
        self.labels.append(tk.Label(text="♠ Piques : Invocation des esprits et des morts",bg="#e0cda9"))
        self.labels[2].place(x=210,y=105)
        self.labels.append(tk.Label(text="♣ Trèfles : Invocation des éléments",bg="#e0cda9"))
        self.labels[3].place(x=210,y=125)

    def init_menu(self,menu):
        
        self.menu_bar=MenuBar(self, menu)
        self.menu_bar.place(x=0,y=0)
        self.menu_bar.pack(fill=tk.X)
        self.menu_bar.configure(bg="#8b6c42")
    
    def init_canvas(self):
        self.canvas_deck=tk.Canvas(bd=0,bg="#e0cda9",width=78, height=122)
        self.canvas_deck.place(x=110,y=45)
        if self.app_deck.card_number!=0:
            img=Image.open(conf.asset_dir+"_#back.png")
            self.img_deck=ImageTk.PhotoImage(image=img) # changes the type of image to make it displayable in the canvas
            self.canvas_deck.create_image(0,0, anchor="nw",image=self.img_deck, tags="img")
            self.canvas_deck["cursor"]='hand2' #change the type of cursor
            self.canvas_deck.bind('<ButtonRelease-1>',self.handle_canvas_click) # bind the mouse "click"
            img.close()
        
        self.canvas_card=tk.Canvas(bd=0,bg="#e0cda9",width=78, height=122)
        self.canvas_card.place(x=10,y=45)

        if len(self.app_deck.discard)!=0:
            img=Image.open(conf.asset_dir+"_#"+self.app_deck.discard[-1][1]+"_"+self.app_deck.discard[-1][0]+".png")
            self.img_discard=ImageTk.PhotoImage(image=img) # changes the type of image to make it displayable in the canvas
            self.canvas_card.create_image(0,0, anchor="nw",image=self.img_discard, tags="img")
            img.close()


    def handle_canvas_click(self,e):
        if self.app_deck.card_number!=0:
            res=self.app_deck.pop_card()
            img=Image.open(conf.asset_dir+"_#"+res[1]+"_"+res[0]+".png")
            self.img_discard=ImageTk.PhotoImage(image=img) # changes the type of image to make it displayable in the canvas
            self.canvas_card.create_image(0,0, anchor="nw",image=self.img_discard, tags="img")
            img.close()
        
        if self.app_deck.card_number==0:
            self.canvas_deck.delete("img")
            self.canvas_deck.unbind('<ButtonRelease-1>')
            self.canvas_deck["cursor"]='arrow' #change the type of cursor
    
    def update_canvas(self):
        if self.app_deck.card_number>=0:
            img=Image.open(conf.asset_dir+"_#back.png")
            self.img_deck=ImageTk.PhotoImage(image=img) # changes the type of image to make it displayable in the canvas
            self.canvas_deck.create_image(0,0, anchor="nw",image=self.img_deck, tags="img")
            self.canvas_deck["cursor"]='hand2' #change the type of cursor
            self.canvas_deck.bind('<ButtonRelease-1>',self.handle_canvas_click) # bind the mouse "click"
            img.close()
        
        if len(self.app_deck.discard)!=0:
            img=Image.open(conf.asset_dir+"_#"+self.app_deck.discard[-1][1]+"_"+self.app_deck.discard[-1][0]+".png")
            self.img_discard=ImageTk.PhotoImage(image=img) # changes the type of image to make it displayable in the canvas
            self.canvas_card.create_image(0,0, anchor="nw",image=self.img_discard, tags="img")
            img.close()
        else :
            self.canvas_card.delete("img")
    



