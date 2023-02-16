file = "day10/day10-input.txt"

#DUDE I HAVE NO IDEA WHAT ITS ASKING ME TO DO LOL

value = 1
tick = 1
list = []
total = 0
#nums = []

with open(file) as f:
    for line in f:
        list.append(line.strip())

# for i in range(len(list) + 1):
#     tick += 1

#     if tick == 20: # or tick == 60 or tick == 100 or tick == 140 or tick == 160 or tick == 180 or tick == 220:
#         total += value * tick
#         break

#     if i < len(list):
#         instruction = list[i]

#         if instruction == 'noop':
#             tick += 1
#             continue

    
#     if i >= 1:
#         if list[i-1][:4] == 'addx':
#             num = int(list[i-1][4:])
#             value += num
#             nums.append(num)

for i in range(len(list)):
    tick += 1
    
    if tick == 20 or tick == 60 or tick == 100 or tick == 140 or tick == 180 or tick == 220:
        total += value * tick

        #print(tick)
        #print(value, value * tick)

        if tick == 60:
            pass
        
        if tick == 220:
            break


    instruction = list[i]

    if instruction == 'noop':
        #tick += 1
        continue

    elif list[i][:4] == 'addx':
        num = int(list[i][4:])
        value += num
        #nums.append(num)
        tick +=1
    
    if tick == 20 or tick == 60 or tick == 100 or tick == 140 or tick == 160 or tick == 180 or tick == 220:
        total += value * tick

        #print(tick)
        #print(value, value * tick)

#print(nums)
print(total)



        

