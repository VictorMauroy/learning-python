""" 
    def : mot clé pour déclarer une fonction
    nbToCheck:int ==> rajouter ":int" permet de déclarer le type de la valeur à recevoir
    "-> None" ==> Permet d'indiquer le type de valeur à retourner. Ici None car pas de "return"    
"""
def IsMyNumberEven(nbToCheck:int) -> None :
    """Determine if a number is even and return a boolean
    
    Keyword arguments:
    nbToCheck -- the number to check"""

    if nbToCheck % 2 == 0:
        print("le nombre est pair")
    else:
        print("le nombre est impair")

"""
IsMyNumberEven(
    int(input("Entrez un nombre entier : "))
    )
"""

def est_pair(nb:int) -> bool :
    """Determine if a number is even and return a boolean"""
    return True if nb%2 == 0 else False

numberOfOurUser = int(input("Veuillez entrer un nombre entier : "))

print(
    "Le nombre est pair" if est_pair(numberOfOurUser) else "Le nombre est impair"
)