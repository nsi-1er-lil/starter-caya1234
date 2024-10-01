#exo 1

import random
taille = random.randit(0,270)
if taille > 150 :
    print(taille, 'cm : Vous pouver entrer, ne vomissez pas svp.')
else:
    print(taille, 'cm : Vous etes trop petits, allez manger de la soupe.')


#exo 2:

def jeu_video(x) :
    votre_sante = 100
    sante_adversaire = 200
    puissance_attaque = 120
    if x <= 2 :
        votre_sante = votre_sante // 2
    elif 3<= x <= 8 :
        sante_adversaire = sante_adversaire - puissance_attaque
    else :
        sante_adversaire = 0
    print('Nombre de :', x,'| Votre sante',votre_sante,'| Sante adverse',sante_adversaire)
jeu_video(2),jeu_video(8),jeu_video(10)


#exo 3

def pokemon_choisi(pokemon):
    if  pokemon == a :
        print('Pokemon choisi : Bulbizarre. Pokemon rival : Carapuce')
    elif pokemon == b:
        print('Pokemon choisi : Carapuce. Pokemon rival : Salameche')
    else :
        print('Pokemon choisi : Salameche. Pokemon rival : Bulbizarre')
a = 'bulbizar'
b = 'carapuce'
c = 'salameche'
pokemon_choisi(a),pokemon_choisi(b), pokemon_choisi(c)