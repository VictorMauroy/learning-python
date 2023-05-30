""" 
    def : mot clé pour déclarer une fonction
    nbToCheck:int ==> rajouter ":int" permet de déclarer le type de la valeur à recevoir
    -> None ==> Permet de déterminer le type de valeur à retourner. Ici None car pas de "return"    
"""
def IsMyNumberEven(nbToCheck:int) -> None :
    """Determine if a number is even and return a boolean
    
    Keyword arguments:
    nbToCheck -- the number to check"""

    if nbToCheck % 2 == 0:
        print("le nombre est pair")
    else:
        print("le nombre est impair")

    #return True if nbToCheck % 2 == 0 else False

IsMyNumberEven(
    int(input("Entrez un nombre entier : "))
    )