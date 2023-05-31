def Threefold_Fivefold_Multiples_Reject() -> None :
    """Show every numbers from 1 to 100 but print Fizz for three-fold multiples and Fuzz for five-fold multiples"""
    for i in range(1, 101) :
        if(i%3 == 0 and i%5 == 0) :
            print("Fizz and... Fuzz !")
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0) :
            print("Fuzz")
        else :
            print(i)

# Correction rapide, je n'ai pas eu le temps d'ajouter la docstring
def fold() :
    for i in range(1, 101) :
        print("i", end = " : ")
        if i%3 == 0 :
            print("Fizz", end = " ")
        if i%5 == 0 :
            print("Fuzz", end = " ")
        print()

Threefold_Fivefold_Multiples_Reject()