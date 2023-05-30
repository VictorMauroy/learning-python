import random
#Do not forger to import "random"
#Useful links : 
# - https://python.doctor/page-comprehension-list-listes-python-cours-debutants
# - https://gayerie.dev/docs/python/python3/list_comprehension.html

randomListOfNumbers = [random.randint(1,100) for _ in range(1000)]
#print(randomListOfNumbers)

smallestNumbersList = [x for x in randomListOfNumbers if x < 10]
print(smallestNumbersList)

anotherSmallestList = []
for elt in randomListOfNumbers :
    if elt < 10 :
        anotherSmallestList.append(elt)
print(anotherSmallestList)