def Get_Average(number1:int, number2:int, number3:int) -> float :
    """Take three numbers and return the average value.

    Returns:
        float: Average value of the three numbers
    """
    return (number1 + number2 + number3) / 3

numbersToCheck = []
for i in range (3):
    numbersToCheck.append(int(input("Veuillez entrer le nombre numéro {} : ".format(i+1))))

print(
    "The average of the three numbers is {}".format(
        Get_Average(numbersToCheck[0], numbersToCheck[1], numbersToCheck[2])
    )
)