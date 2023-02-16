
def overlap(e1, e2):
    e1Val1 = int(e1[0])
    e1Val2 = int(e1[1])

    e2Val1 = int(e2[0])
    e2Val2 = int(e2[1])

    if ((e1Val1 >= e2Val1) and (e1Val1 <= e2Val2)) or ((e2Val1 >= e1Val1) and (e2Val1 <= e1Val2)) or ((e1Val2 <= e2Val2) and (e1Val2 >= e2Val1)) or ((e2Val2 <= e1Val2) and (e2Val2 >= e1Val1)):
        return True

    # if ((e1Val1 >= e2Val1) and (e1Val2 <= e2Val2)) or ((e2Val1 >= e1Val1) and (e2Val2 <= e1Val2)):
    #     return True


total = 0

with open("day4/day4-input.txt") as f:
    for line in f:
        splitL = line.strip().split(",")
        elf1 = splitL[0].split("-")
        elf2 = splitL[1].split("-")

        #print(elf1, elf2)

        if overlap(elf1, elf2):
            #print(elf1, elf2)
            total += 1

print(total)

