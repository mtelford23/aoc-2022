
def parseTable(fpath):
    opponentPlays = []
    yourPlays = []

    with open(fpath) as f:
        for line in f:
            l = line.strip()
            #print(l)

            opponentPlays.append(l[:1])
            yourPlays.append(l[1:].strip())

    opponentPlays = decryptOpponentPlays(opponentPlays)

    return opponentPlays, yourPlays

def decryptOpponentPlays(list):
    newList = []

    for x in list:
        if x == 'A':
            newList.append('R')

        elif x == 'B':
            newList.append('P')

        elif x == 'C':
            newList.append('S')

    return newList

def pointsForRound(opp, you):
    if you == 'Y':
        return 3 + pointForPlay(opp)
    elif you == 'X':
        return 0 + pointForPlay(whatNeededToLose(opp))
    elif you == 'Z':
        return 6 + pointForPlay(whatNeededToWin(opp))

def pointForPlay(letter):
    if letter == 'S':
        return 3
    elif letter == 'P':
        return 2
    else:
        return 1

def whatNeededToLose(letter):
    if letter == 'S':
        return 'P'
    elif letter == 'P':
        return 'R'
    elif letter == 'R':
        return 'S'

def whatNeededToWin(letter):
    if letter == 'S':
        return 'R'
    elif letter == 'P':
        return 'S'
    elif letter == 'R':
        return 'P'

def results(list):
    total = 0
    oppPlays = plays[0]
    yourPlays = plays[1]

    counter = 0;
    for y in yourPlays:
        #print(y)
        total += pointsForRound(oppPlays[counter], y)
        counter += 1

    return total

plays = parseTable("day2/day2-input.txt")

print(results(plays))


