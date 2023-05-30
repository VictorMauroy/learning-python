### Before ###
def x(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return a*b

### After ###

def Absolute_Multiplication(numberA:int, numberB:int) -> int :
    """Multiply two numbers and return the absolute result

    Args:
        numberA (int): First number
        numberB (int): Second number

    Returns:
        int: Absolute result of the multiplication of numberA and numberB
    """
    if(numberA < 0) :
        numberA = -numberA
    if(numberB < 0) :
        numberB = -numberB
    return numberA*numberB