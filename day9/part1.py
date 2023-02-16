f = "day9/day9-input.txt"

H = [0, 0]
T = [0, 0]

visited = {"0,0"}

def TnearHAndUpdate():
    if H[0] != T[0] and H[1] != T[1]: #diagonal situation
        if (H[0] - T[0] >= 1 and H[1] - T[1] > 1) or (H[0] - T[0] > 1 and H[1] - T[1] >= 1):
            T[0] += 1
            T[1] += 1
        
        elif (H[0] - T[0] <= -1 and H[1] - T[1] > 1) or (H[0] - T[0] < -1 and H[1] - T[1] >= 1):
            T[0] -= 1
            T[1] += 1

        elif (H[0] - T[0] <= -1 and H[1] - T[1] < -1) or (H[0] - T[0] < -1 and H[1] - T[1] <= -1):
            T[0] -= 1
            T[1] -= 1

        elif (H[0] - T[0] >= 1 and H[1] - T[1] < -1) or (H[0] - T[0] > 1 and H[1] - T[1] <= -1):
            T[0] += 1
            T[1] -= 1

    else:
        if H[0] - T[0] > 1:
            T[0] += 1
    
        elif H[0] - T[0] < -1:
            T[0] -= 1
            
        if H[1] - T[1] > 1:
            T[1] += 1

        elif H[1] - T[1] < -1:
            T[1] -= 1
            

with open(f) as file:
    for line in file:
        linesplit = line.strip().split(" ")
        dir = linesplit[0]
        num = int(linesplit[1])

        if dir == 'R':
            endpt = H[0] + num

            while H[0] < endpt:
                H[0] += 1

                TnearHAndUpdate()
                visited.add(str(T[0]) + "," + str(T[1]))

                #r += 1

        elif dir == 'L':
            endpt = H[0] - num

            while H[0] > endpt:
                H[0] -= 1

                TnearHAndUpdate()
                visited.add(str(T[0]) + "," + str(T[1]))

                # l += 1

        elif dir == 'U':
            endpt = H[1] + num

            while H[1] < endpt:
                H[1] += 1

                TnearHAndUpdate()
                visited.add(str(T[0]) + "," + str(T[1]))

                # u += 1

        elif dir == 'D':
            endpt = H[1] - num

            while H[1] > endpt:
                H[1] -= 1

                TnearHAndUpdate()
                visited.add(str(T[0]) + "," + str(T[1]))

                # r += 1

        #print(len(visited))

#print(visited)
print(len(visited))