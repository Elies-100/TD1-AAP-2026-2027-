#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import sys
import os

def lire():
    if len(sys.argv)>1:
        try:
            flux=open(sys.argb[1],"r")
        except:
            sys.exit("Erreur" + sys.argv[1])
        texte=flux.read()
        flux.close()
    else:
        texte = sys.stdin.read()
    return texte

texte=lire()
caractere=0
ligne=0
mot=0
dans_mot=False
for a in texte:
    caractere+=1
    match a:
        case"\n":
            ligne+=1
            dans_mot=False
        case ""| "\t":
            dans_mot=False
        case _:
            if not dans_mot:
                dans_mot=True
                mot+=1
                if "DEBUG" in os.environ:
                        print("mot", mot, file=sys.stderr)

print(ligne, mot, caractere)
    
# récupération des arguments et sélection du flux
    # parcours du flux
    # comptage
    # affichage 
    
    


if __name__ == "__main__":
    lire()
