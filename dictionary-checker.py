# Do not mind me for the content of the dictionary !
CharactersElement = {
    "Jing Yuan" : "Lightning",
    "Himeko" : "Fire",
    "Welt" : "Imaginary",
    "Yanqing" : "Ice",
    "Seele" : "Quantic",
    "Bronya" : "Wind",    
}

def Check_In_Dictionary(searchedCharacter:str):
    """Check in the character dictionary and return the element of the latter if finded  

    Args:
        character (str): Name of the character that we want to obtain the element
    """
    characterFinded = False
    for name, powerElement in CharactersElement.items():
        if(name == searchedCharacter) :
            print("L'élement du personnage est : {}.".format(powerElement))
            return
    print("Nous n'avons pas trouvé ce personnage.")

characterToSearch = str(input("Entrez le nom d'un personnage pour trouver son élément : "))
Check_In_Dictionary(characterToSearch)