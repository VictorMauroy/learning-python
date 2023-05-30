def Sum(numbers:list) -> int :
    """Return the sum of all the numbers in the list

    Args:
        numbers (list): List of numbers to addition

    Returns:
        int: Sum of all the numbers
    """
    sumValue = 0
    for elt in numbers :
        sumValue += elt
    return sumValue

def Average_From_List(numbers:list) -> float :
    """Create an average value from a list of numbers"""
    sumValue = float(Sum(numbers))
    return sumValue / float(len(numbers))
#len() allows to obtain the length of a list

listOfNumbers = [5, 18, 20, 15, 16, 12]
print(
    "Moyenne des valeurs de la liste : {}".format(
        Average_From_List(listOfNumbers)
    )
)