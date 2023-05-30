var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

## Ajouter le code de l'exercice ici ##

"""
Method 1 : creating a temporary variable
temp = var1
var1 = var2
var2 = temp
"""

# Method 2 : 
var1, var2 = var2, var1

print(var1 + " | " + var2) 
# après avoir complété l'exercice, doit afficher :
# Je dois être en première position | Je dois être en seconde position