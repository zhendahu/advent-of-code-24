def main():
    input = open('day1_input.txt', 'r')
    lines = input.readlines()
    list1, list2 = [], []
    for line in lines:
        split = line.split('   ')
        list1.append(int(split[0]))
        list2.append(int(split[1]))
    input.close()
    list1.sort()
    list2.sort()

    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])

    print(diff)


if __name__ == '__main__':
    main()