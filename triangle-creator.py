def Make_Triangle(triangleSize:int) -> None :
    """Make a triangle of '#' with a size specified by triangleSize

    Args:
        triangleSize (int): Heigh of the triangle
    """
    if triangleSize == 0 : return
    for i in range(0, triangleSize) : 
        message = "#"
        for j in range(i):
            message += "#"
        print(message)

# Correction


Make_Triangle(
    int(
        input("Entrez la taille du triangle désiré : ")
        )
    )