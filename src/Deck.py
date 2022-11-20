import config as conf
import random
import json


class Deck():
    def __init__(self) -> None:
        self.load_deck()    
        self.card_number=len(self.deck)

    def generate_new_deck(self,nbr,to_add=[[]],to_avoid=[[]]):
        n=len(to_add)
        self.card_number=nbr
        self.deck=[]
        self.discard=[]
        if type(to_add[0])==list :
            if to_add[0]!=[] :
                self.deck+=to_add
        elif type(to_add)==list : 
            self.deck.append(to_add)

        if type(to_avoid[0])!=list:
            to_avoid=[to_avoid]

        full_deck_cp=conf.full_deck.copy()
        len_full_deck=conf.len_deck

        i=random.randint(1,7)
        for k in range(i):
            random.shuffle(full_deck_cp)

        for k in range(nbr-n+1) :
            val=full_deck_cp[random.randrange(0,len_full_deck)]
            while((val in to_avoid) or (val in self.deck)):
                val=full_deck_cp[random.randrange(0,len_full_deck)]
            
            self.deck.append(val)
            full_deck_cp.remove(val)
            len_full_deck-=1
        
        random.shuffle(self.deck)


    def add_card(self,from_discard=False, rand=False,card=["joker","black"]) ->None:
        if from_discard : 
            try:
                discard=self.discard.copy()
                i=random.randint(1,7)
                random.shuffle(discard)
                for k in range(i):
                    random.shuffle(discard)
                val=discard[random.randrange(0,len(discard))]
                self.deck.append(val)
                self.discard.remove(val)
                print("yeah")
            except ValueError :
                full_deck_cp=conf.full_deck.copy()
                val=full_deck_cp[random.randrange(0,conf.len_deck)]
                while((val in self.deck)):
                    val=full_deck_cp[random.randrange(0,conf.len_deck)]
                self.deck.append(val)
        else :
            if rand : 
                full_deck_cp=conf.full_deck.copy()
                val=full_deck_cp[random.randrange(0,conf.len_deck)]
                while((val in self.deck)):
                    val=full_deck_cp[random.randrange(0,conf.len_deck)]
                self.deck.append(val)
            else : 
                self.deck.append(card)
        self.card_number+=1
        
    def pop_card(self):
        try : 
            self.discard.append(self.deck.pop())
            self.card_number-=1
            return self.discard[-1]
        except IndexError :
            print("Your deck is already empty")
            return None

    def shuffle(self, iteration=1) :
        for k in range(iteration):
            random.shuffle(self.deck)
        
    def save_deck(self):
        dic={"deck": self.deck,
             "discard":self.discard}
        with open("deck.json","w") as jsonFile:
            jsonString= json.dumps(dic)
            jsonFile.write(jsonString)


    def load_deck(self):
        with open("deck.json","r") as jsonFile:
            jsonContent= jsonFile.read()
            if jsonContent!="":
                obj_python=json.loads(jsonContent)
            else : 
                obj_python={"deck": [],"discard": []}

            self.deck=obj_python["deck"]
            self.discard=obj_python["discard"]




