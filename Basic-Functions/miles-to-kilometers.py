#hello = "Bonjour"
#enterMessage = "veuillez entrer une valeur"
#print(hello, ", ", enterMessage)

#Ne pas oublier de convertir en float pour pouvoir réaliser le calcul ensuite
milesValue = float(input('Bonjour, veuillez entrer une valeur en miles : ')) 

kilometerResult = milesValue * 1.609

print(milesValue, " miles est équivalent à ", kilometerResult, " km")