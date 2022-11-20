import os

my_os=os.name

if my_os=="posix" :
    asset_dir="assets/"
elif my_os=="nt" :
    asset_dir="assets\\"

color=["club","spade","heart","diamond" ]

value=["2","3","4","5","6","7","8","9","10","jack","queen","king","1"]

full_deck=[]

len_deck=4*13

for i in range(13):
    for k in range(4):
        full_deck.append([color[k],value[i]])

equivalence={"as de pique": ["spade","1"],
            "deux de pique": ["spade","2"],
            "trois de pique": ["spade","3"],
            "quatre de pique": ["spade","4"],
            "cinq de pique": ["spade","5"],
            "six de pique": ["spade","6"],
            "sept de pique": ["spade","7"],
            "huit de pique": ["spade","8"],
            "neuf de pique": ["spade","9"],
            "dix de pique": ["spade","10"],
            "valet de pique": ["spade","jack"],
            "dame de pique": ["spade","queen"],
            "roi de pique": ["spade","king"],
            "as de trèfle": ["club","1"],
            "deux de trèfle": ["club","2"],
            "trois de trèfle": ["club","3"],
            "quatre de trèfle": ["club","4"],
            "cinq de trèfle": ["club","5"],
            "six de trèfle": ["club","6"],
            "sept de trèfle": ["club","7"],
            "huit de trèfle": ["club","8"],
            "neuf de trèfle": ["club","9"],
            "dix de trèfle": ["club","10"],
            "valet de trèfle": ["club","jack"],
            "dame de trèfle": ["club","queen"],
            "roi de trèfle": ["club","king"],
            "as de coeur": ["heart","1"],
            "deux de coeur": ["heart","2"],
            "trois de coeur": ["heart","3"],
            "quatre de coeur": ["heart","4"],
            "cinq de coeur": ["heart","5"],
            "six de coeur": ["heart","6"],
            "sept de coeur": ["heart","7"],
            "huit de coeur": ["heart","8"],
            "neuf de coeur": ["heart","9"],
            "dix de coeur": ["heart","10"],
            "valet de coeur": ["heart","jack"],
            "dame de coeur": ["heart","queen"],
            "roi de coeur": ["heart","king"],
            "as de carreau": ["diamond","1"],
            "deux de carreau": ["diamond","2"],
            "trois de carreau": ["diamond","3"],
            "quatre de carreau": ["diamond","4"],
            "cinq de carreau": ["diamond","5"],
            "six de carreau": ["diamond","6"],
            "sept de carreau": ["diamond","7"],
            "huit de carreau": ["diamond","8"],
            "neuf de carreau": ["diamond","9"],
            "dix de carreau": ["diamond","10"],
            "valet de carreau": ["diamond","jack"],
            "dame de carreau": ["diamond","queen"],
            "roi de carreau": ["diamond","king"],
            "joker noir": ["joker","black"],
            "joker rouge": ["joker","red"],
            "joker": ["joker","black"]
           }



