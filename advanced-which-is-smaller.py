def Determine_Smallest_Number(nb1:int, nb2:int, nb3:int) -> int:
    """Determine which number is the smallest between three and return it"""
    if (nb1 <= nb2 and nb1 <= nb3):
        return nb1
    elif (nb2 <= nb1 and nb2 <= nb3):
        return nb2
    else : return nb3

numbersToCheck = []
for i in range (3):
    numbersToCheck.append(int(input("Veuillez entrer le nombre numéro {} : ".format(i+1))))

# "elt" à la place de "i", ici i n'est pas un entier mais prend directement les valeurs à chaque occurence.
# elt va donc être le premier élement (nombre) puis le second nombre, etc. On peut le renommer.
"""
for elt in numbersToCheck :
    print(elt)
"""
print(
    "The smallest number is : {}".format(
Determine_Smallest_Number(numbersToCheck[0], numbersToCheck[1], numbersToCheck[2]))
)