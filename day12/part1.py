file = "day12/day12-input.txt"

landscape = []
eCoords = []
sCoords = []

with open(file) as f:
    r = 0

    for line in f:
        c = 0

        for char in line.strip():
            if char == 'E':
                eCoords = [c, r]

            if char == 'S':
                sCoords = [c, r]

            if r == 0:
                landscape.append([char])

            else:
                landscape[c].append(char)
                c += 1

        r += 1

rLen = len(landscape[0])
cLen = len(landscape)

def availablePath(c, r, dir):
    if dir == 'U':
        if r == 0:
            return False
    
        if landscape[c][r] == 'z' and landscape[c][r+1] == 'E':
            return True

        elif abs(ord(landscape[c][r]) - ord(landscape[c][r-1])) == 1 or (ord(landscape[c][r]) - ord(landscape[c][r-1]) == 0):
            return True

    if dir == 'D':
        if r == rLen - 1:
            return False

        if landscape[c][r] == 'z' and landscape[c][r-1] == 'E':
            return True

        elif abs(ord(landscape[c][r]) - ord(landscape[c][r+1])) == 1 or (ord(landscape[c][r]) - ord(landscape[c][r+1]) == 0):
            return True

    if dir == 'L':
        if c == 0:
            return False

        if landscape[c][r] == 'z' and landscape[c-1][r] == 'E':
            return True

        elif abs(ord(landscape[c][r]) - ord(landscape[c-1][r])) == 1 or ord(landscape[c][r]) - ord(landscape[c-1][r]) == 0:
            return True

    if dir == 'R':
        if c == cLen - 1:
            return False

        if landscape[c][r] == 'z' and landscape[c+1][r] == 'E':
            return True

        elif abs(ord(landscape[c][r]) - ord(landscape[c+1][r])) == 1 or ord(landscape[c][r]) - ord(landscape[c+1][r]) == 0:
            return True

    return False

stepCount = 0

r = sCoords[1]
c = sCoords[0]
curr = landscape[c][r]


print("here")
while curr != 'E': #need to take out this or statement, also need to change chars to mark which have already been visited?
    if stepCount == 60:
        pass
    
    if curr == 'S':
        landscape[c][r] = ""

        if eCoords[0] > eCoords[1]:
            c += 1
        
        else:
            r += 1
    
        curr = landscape[c][r]

    elif curr == 'E':
        break

    else:
        if availablePath(c, r, 'R'):
            landscape[c][r] = " "
            c += 1

        elif availablePath(c, r, 'D'):
            landscape[c][r] = " "
            r += 1

        elif availablePath(c, r, 'L'):
            landscape[c][r] = " "
            c -= 1

        elif availablePath(c, r, 'U'):
            landscape[c][r] = " "
            r -= 1
    
    
        curr = landscape[c][r]

    stepCount += 1
    print(stepCount, curr, "(", c, ",", r, ")")

print(stepCount, "(", c, ",", r, ")")
