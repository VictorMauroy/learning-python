awesomeList = [1, "test", 0.9867, "Python, c'est génial !"]

def Revert_List(listToReverse:list) -> list:
    """Revert a list content and return its"""
    revertedList = []
    listLength = len(listToReverse)
    print(listLength)
    for i in range(1, listLength+1) :
        revertedList.append(listToReverse[listLength-i])
    return revertedList

print(Revert_List(awesomeList))