# import random
#Do not forger to import "random"
#Useful links : 
# - https://python.doctor/page-comprehension-list-listes-python-cours-debutants
# - https://gayerie.dev/docs/python/python3/list_comprehension.html

from random import randint 
#Permet d'importer uniquement une partie de la librairie random

randomListOfNumbers = [randint(1,100) for _ in range(1000)]
#print(randomListOfNumbers)

smallestNumbersList = [elt for elt in randomListOfNumbers if elt < 10]
print(smallestNumbersList)

anotherSmallestList = []
for elt in randomListOfNumbers :
    if elt < 10 :
        anotherSmallestList.append(elt)
print(anotherSmallestList)