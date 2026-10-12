#! /usr/bin/env python3
"""Programme permettant de récupérer le pseudo de l'utilisateur saisi au clavier et de le saluer : ***Bonjour [pseudo] !***. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import sys
def saisie():
    name=sys.stdin.read()

    print("\n Bonjour", name, "!")
    return ""

if __name__ == "__main__":
    saisie()
