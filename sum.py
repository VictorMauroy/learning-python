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

listOfNumbers = [5, 18, 20, 15, 16, 12]

print(Sum(listOfNumbers))