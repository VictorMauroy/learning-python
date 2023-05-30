def Threefold_Fivefold_Multiples_Reject() -> None :
    """Show every numbers from 1 to 100 but print Fizz for three-fold multiples and Fuzz for five-fold multiples"""
    for i in range(1, 101) :
        if(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0) :
            print("Fuzz")
        else :
            print(i)

Threefold_Fivefold_Multiples_Reject()