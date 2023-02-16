def commonItemPriority(letter):
        ciAscii = ord(letter)
        priority = 0

        if ciAscii <= 122 and ciAscii >= 97: #for lower case, in ascii
            priority = ciAscii - 96

        elif ciAscii <= 90 and ciAscii >= 65:
            priority = ciAscii - 38

        return priority

def commonItem(l1, l2, l3):
    for letter in l1:
        if l2.find(letter) != -1 and l3.find(letter) != -1:
            #print(letter)
            return letter

total = 0
counter = 0

# with open("day3/day3-test.txt") as f:
#     for line in f:
#         print("counter is: ")
#         print(counter)

#         if counter < len(f.readlines()) - 2 and counter % 3 == 0:
#             l1 = line.strip()
#             l2 = next(f).strip()
#             l3 = next(next(f)).strip()
            
#             ip = commonItemPriority(commonItem(l1, l2, l3))
#             #print(ip)
#             total += ip
            
#         counter += 1


with open("day3/day3-input.txt") as f:
    lines = f.readlines()

for i in range(len(lines) - 2):
    if counter % 3 == 0:
        l1 = lines[counter].strip()
        l2 = lines[counter + 1].strip()
        l3 = lines[counter + 2].strip()
        
        ip = commonItemPriority(commonItem(l1, l2, l3))
        #print(ip)
        total += ip
            
    counter += 1


print(total)