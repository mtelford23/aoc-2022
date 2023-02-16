
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
    yourPlays = decryptYourPlays(yourPlays)

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

def decryptYourPlays(list):
    newList = []

    for x in list:
        if x == 'X':
            newList.append('R')

        elif x == 'Y':
            newList.append('P')

        elif x == 'Z':
            newList.append('S')

    return newList

def didYouWinMatch(opp, you):
    if opp == you:
        return 3 #tie

    elif opp == 'R' and you == 'P':
        return 6 #won
    
    elif opp == 'P' and you =='S':
        return 6 #won
    
    elif opp == 'S' and you == 'R':
        return 6 #won

    else:
        return 0 #loss

def pointsForPlay(letter):
    if letter == 'S':
        return 3
    elif letter == 'P':
        return 2
    else:
        return 1

def results(list):
    total = 0
    oppPlays = plays[0]
    yourPlays = plays[1]

    counter = 0;
    for y in yourPlays:
        #print(y)
        total += didYouWinMatch(oppPlays[counter], y)
        total += pointsForPlay(y)
        counter += 1

    return total

plays = parseTable("day2/day2-input.txt")

print(results(plays))


