
def totalList(list):
    total = 0;
    
    for x in list:
        total += x

    return total

def populateListOfTotals(fpath):
    listOfTotals = []

    with open(fpath) as f:
        currentTotal = 0

        for line in f:
            currLine = line.strip()
            #print(currLine)

            if (currLine == ''):
                #print(currentTotal)
                listOfTotals.append(currentTotal)
                currentTotal = 0;
            else:
                currentTotal += int(currLine)

        listOfTotals.append(currentTotal)
                
    f.close()
    return listOfTotals

def findSingleMax(list):
    max = 0
    for x in list:
        if x > max:
            max = x

    return max

def findThreeMax(list):
    max1 = findSingleMax(list)
    max2 = 0
    max3 = 0

    for x in list:
        if (x < max1 and x > max2):
            max2 = x
            print(max2)
    
    for x in list:
        if (x < max1 and x < max2 and x > max3):
            max3 = x
            print(max3)

    return [max1, max2, max3]

totalsList = populateListOfTotals("day1/day1-input.txt")
threeMax = findThreeMax(totalsList)

print("single max: ")
print(findSingleMax(totalsList))
print()
print("three maxs:")
print(threeMax[0])
print(threeMax[1])
print(threeMax[2])
print()
print("total three max:")
print(totalList(threeMax))



