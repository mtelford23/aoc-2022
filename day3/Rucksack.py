from typing import Self

class Rucksack:
    compartment1 = ""
    compartment2 = ""
    commonItem = ''

    def __init__(self, contents):
        midpoint = int(len(contents)/2)
        self.compartment1 = contents[:midpoint]
        self.compartment2 = contents[midpoint:]
        self.commonItem = self.findCommonItem()

    def findCommonItem(self):
        for letter in self.compartment1:
            if self.compartment2.find(letter) != -1:
                #print(letter)
                return letter
    
