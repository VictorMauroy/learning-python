#hello = "Bonjour"
#enterMessage = "veuillez entrer une valeur"
#print(hello, ", ", enterMessage)

#Ne pas oublier de convertir en float pour pouvoir réaliser le calcul ensuite
# milesValue = float(input('Bonjour, veuillez entrer une valeur en miles : ')) 

# kilometerResult = milesValue * 1.609

# print(milesValue, " miles est équivalent à ", kilometerResult, " km")

# Correction
input_user = input("Please enter a distance in (miles)")
try :
    input_user = int(input_user)
except ValueError :
    print("I ask for a number...")
except TypeError:
    pass

kilometerResult = input_user * 1.609

print(input_user, " miles est équivalent à ", kilometerResult, " km")

#Userful link : https://docs.python.org/fr/3/tutorial/errors.html