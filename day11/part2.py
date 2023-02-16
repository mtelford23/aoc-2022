class monky:
    def __init__(self, items, operation, test, t, f):
        self.items = []
        for i in range(len(items)):
            self.items.append(int(items[i]))

        self.operation = operation #string
        self.testOp = test
        self.t = int(t)
        self.f = int(f)
        self.numInspects = 0

    #takes in the item and does the operation and return the item number and worry level div by three bc monky gets bored
    def inspect(self):
        item = self.items[0]

        self.numInspects += 1
        
        opSign = self.operation.split(" ")[0]
        opNum = self.operation.split(" ")[1]

        newNum = 999

        if opNum == "old":
            opNum = item

        else:
            opNum = int(opNum)

        if opSign == '+':
             newNum = item + opNum

        elif opSign == '-':
            newNum = item - opNum

        elif opSign == '*':
            newNum = item * opNum

        elif opSign == '/':
            newNum = item / opNum

        else: 
            print("unrecognizable operation sign")

        return self.throw(item, newNum%supermod)

        #print(item, int(newNum/3))

    #tests with the test op, return the number of the monky it throws the item to and removes item from current monky list
    def throw(self, item, worryLevel):
        self.items.remove(item)

        if divmod(worryLevel, self.testOp)[1] == 0:
            return self.t, worryLevel

        else:
            return self.f, worryLevel

    #appends item to item list 
    def catch(self, item):
        self.items.append(item)
        


file = "day11/day11-input.txt"
monkies = []

with open(file) as f:
    lines = f.readlines()

supermod = 1
testList = []
i = 0
while i < len(lines):
    if lines[i].strip()[:1] == 'M':
        items = lines[i+1].strip().split(": ")[1].split(", ")
        operation = lines[i+2].strip().split("old ")[1]
        test = int(lines[i+3].strip().split("by ")[1])
        testList.append(test)
        trueCase = lines[i+4].strip().split("monkey ")[1]
        falseCase = lines[i+5].strip().split("monkey ")[1]
        monkies.append(monky(items, operation, test, trueCase, falseCase))

    i += 1

for k in range(len(testList)):
    supermod *= testList[k]

for round in range(10000):
    for m in range(len(monkies)):
        for k in range(len(monkies[m].items)):
            thrownTo = monkies[m].inspect()
            monkies[thrownTo[0]].catch(thrownTo[1])

mostInspects1 = 0
monkyNum1 = 999

mostInspects2 = 0
monkyNum2 = 999

for m in range(len(monkies)):
    thisMonkInsp = monkies[m].numInspects
    #print(thisMonkInsp)

    if thisMonkInsp >= mostInspects1:
        monkyNum1 = m
        mostInspects1 = thisMonkInsp

for m in range(len(monkies)):
    thisMonkInsp = monkies[m].numInspects

    if thisMonkInsp >= mostInspects2 and m != monkyNum1:
        monkyNum2 = m
        mostInspects2 = thisMonkInsp

print(mostInspects2 * mostInspects1)