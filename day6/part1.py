with open("day6/day6-input.txt") as f:
    l = f.read()

counter = 0

for i in range(len(l) - 3): #unsure about the -3 part
    counter += 1

    fourChar = l[i : i + 4]
    repChars = False
    #print(fourChar)

    for k in range(4):
        #print(fourChar.count(fourChar[k]), fourChar[k])
        if fourChar.count(fourChar[k]) != 1:
            repChars = True
            break

    if not repChars:
        counter += 3
        print(counter)
        break
