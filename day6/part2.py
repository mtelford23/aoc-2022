with open("day6/day6-input.txt") as f:
    l = f.read()

counter = 0

for i in range(len(l) - 3): #unsure about the -3 part
    counter += 1

    chars = l[i : i + 14]
    repChars = False
    #print(fourChar)

    for k in range(14):
        #print(fourChar.count(fourChar[k]), fourChar[k])
        if chars.count(chars[k]) != 1:
            repChars = True
            break

    if not repChars:
        counter += 13
        print(counter)
        break
