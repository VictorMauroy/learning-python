firstNumber = int(input("Votre premier nombre : "))
secondNumber = int(input("Votre second nombre : "))
thirdNumber = int(input("Votre troisième nombre : "))

if firstNumber >= secondNumber and firstNumber >= thirdNumber :
    print("Your FIRST number is the greater : {}" .format(firstNumber)) #One way to integrate our value
elif secondNumber >= firstNumber and secondNumber >= thirdNumber :
    print("Your SECOND number is the greater : ", secondNumber) # Classic way
else:
    print("Your THIRD number is the greater : {0}".format(thirdNumber)) #Another way