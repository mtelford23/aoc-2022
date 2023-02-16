f = "day9/day9-input.txt"

H = [0, 0]
T0 = [0, 0]
T1 = [0, 0]
T2 = [0, 0]
T3 = [0, 0]
T4 = [0, 0]
T5 = [0, 0]
T6 = [0, 0]
T7 = [0, 0]
T8 = [0, 0]
T9 = [0, 0]

visited = {"0,0"}

def TnearHAndUpdate(L1, L2):
    if L1[0] != L2[0] and L1[1] != L2[1]: #diagonal situation
        if (L1[0] - L2[0] >= 1 and L1[1] - L2[1] > 1) or (L1[0] - L2[0] > 1 and L1[1] - L2[1] >= 1):
            L2[0] += 1
            L2[1] += 1
        
        elif (L1[0] - L2[0] <= -1 and L1[1] - L2[1] > 1) or (L1[0] - L2[0] < -1 and L1[1] - L2[1] >= 1):
            L2[0] -= 1
            L2[1] += 1

        elif (L1[0] - L2[0] <= -1 and L1[1] - L2[1] < -1) or (L1[0] - L2[0] < -1 and L1[1] - L2[1] <= -1):
            L2[0] -= 1
            L2[1] -= 1

        elif (L1[0] - L2[0] >= 1 and L1[1] - L2[1] < -1) or (L1[0] - L2[0] > 1 and L1[1] - L2[1] <= -1):
            L2[0] += 1
            L2[1] -= 1

    else:
        if L1[0] - L2[0] > 1:
            L2[0] += 1
    
        elif L1[0] - L2[0] < -1:
            L2[0] -= 1
            
        if L1[1] - L2[1] > 1:
            L2[1] += 1

        elif L1[1] - L2[1] < -1:
            L2[1] -= 1

    #visited.add(str(L2[0]) + "," + str(L2[1]))
            

with open(f) as file:
    for line in file:
        linesplit = line.strip().split(" ")
        dir = linesplit[0]
        num = int(linesplit[1])

        if dir == 'R':
            endpt = H[0] + num

            while H[0] < endpt:
                H[0] += 1

                TnearHAndUpdate(H, T0)
                TnearHAndUpdate(T0, T1)
                TnearHAndUpdate(T1, T2)
                TnearHAndUpdate(T2, T3)
                TnearHAndUpdate(T3, T4)
                TnearHAndUpdate(T4, T5)
                TnearHAndUpdate(T5, T6)
                TnearHAndUpdate(T6, T7)
                TnearHAndUpdate(T7, T8)
                visited.add(str(T8[0]) + "," + str(T8[1]))

                #r += 1

        elif dir == 'L':
            endpt = H[0] - num

            while H[0] > endpt:
                H[0] -= 1

                TnearHAndUpdate(H, T0)
                TnearHAndUpdate(T0, T1)
                TnearHAndUpdate(T1, T2)
                TnearHAndUpdate(T2, T3)
                TnearHAndUpdate(T3, T4)
                TnearHAndUpdate(T4, T5)
                TnearHAndUpdate(T5, T6)
                TnearHAndUpdate(T6, T7)
                TnearHAndUpdate(T7, T8)
                visited.add(str(T8[0]) + "," + str(T8[1]))

                # l += 1

        elif dir == 'U':
            endpt = H[1] + num

            while H[1] < endpt:
                H[1] += 1

                TnearHAndUpdate(H, T0)
                TnearHAndUpdate(T0, T1)
                TnearHAndUpdate(T1, T2)
                TnearHAndUpdate(T2, T3)
                TnearHAndUpdate(T3, T4)
                TnearHAndUpdate(T4, T5)
                TnearHAndUpdate(T5, T6)
                TnearHAndUpdate(T6, T7)
                TnearHAndUpdate(T7, T8)
                visited.add(str(T8[0]) + "," + str(T8[1]))

                # u += 1

        elif dir == 'D':
            endpt = H[1] - num

            while H[1] > endpt:
                H[1] -= 1

                TnearHAndUpdate(H, T0)
                TnearHAndUpdate(T0, T1)
                TnearHAndUpdate(T1, T2)
                TnearHAndUpdate(T2, T3)
                TnearHAndUpdate(T3, T4)
                TnearHAndUpdate(T4, T5)
                TnearHAndUpdate(T5, T6)
                TnearHAndUpdate(T6, T7)
                TnearHAndUpdate(T7, T8)
                visited.add(str(T8[0]) + "," + str(T8[1]))

                # r += 1

        #print(len(visited))

#print(visited)
print(len(visited))