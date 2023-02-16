from Rucksack import Rucksack

def commonItemPriority(rs):
        ciAscii = ord(getattr(rs, "commonItem"))
        priority = 0

        if ciAscii <= 122 and ciAscii >= 97: #for lower case, in ascii
            priority = ciAscii - 96

        elif ciAscii <= 90 and ciAscii >= 65:
            priority = ciAscii - 38

        return priority

total = 0

with open("day3/day3-input.txt") as f:
    for line in f:
        l = line.strip()
        #print(l)
        r = Rucksack(l)
        ip = commonItemPriority(r)
        #print(ip)
        total += ip

print(total)

