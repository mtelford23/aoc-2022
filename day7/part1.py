file = "day7/day7-input.txt"

##TODO: PROBLEM IS THAT DIRS CAN HAVE REPEAT NAMES IF THEY AREN'T INSIDE THE SAME PARENT
with open(file) as f:
    directories = []
    inADir = False
    new = []

    for line in f:

        if line.__contains__("$ cd"):
            if line.__contains__(".."):
                continue

            if len(new) > 1:
                directories.append(new)

            new = [line.strip().split(" ")[2]]
            inADir = True
            continue

        if inADir:
            if line.__contains__("$ ls"):
                continue

            if line.__contains__("dir"):
                new.append(line.strip().split(" ")[1])
                continue

            new.append(line.strip())

    directories.append(new)

#print(directories)

files = []
dirNames = []
dirContains = []
#am I overcomplicating this? maybe a little

for i in directories:
    dirNames.append(i[0])
    i.pop(0)

    newFiles = []
    newDirContains = []

    for k in i:
        if not k.__contains__(" "):
            newDirContains.append(k)

        else:
            newFiles.append(int(k.split(" ")[0]))

    total = 0
    for t in newFiles:
        total += t

    files.append(total)
    dirContains.append(newDirContains)

# print("")
# print(files)
# print(dirNames)
# print(dirContains)

# print("")
for i in range(len(dirNames)):
    toAdd = 0

    if dirNames[i] == '/':
        fullTotal = 0
        for q in files:
            fullTotal += q
        
        files[i] = fullTotal

    elif len(dirContains[i]) != 0:
        for l in dirContains[i]:
            toAdd += files[dirNames.index(l)]
    
    files[i] += toAdd

# print(files)
# print(dirNames)

actualTotal = 0
for i in files:
    if i <= 100000:
        actualTotal += i

print(actualTotal)