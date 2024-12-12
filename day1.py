input = open('day1_input.txt', 'r')
lines = input.readlines()
list1, list2 = [], []
for line in lines:
    split = line.split('   ')
    list1.append(int(split[0]))
    list2.append(int(split[1]))
input.close()

def part1(list1, list2):
    list1.sort()
    list2.sort()

    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])

    print(diff)

def part2(list1, list2):
    score = 0
    for num in list1:
        count = list2.count(num)
        score += count * num
    
    print(score)

part2(list1, list2)