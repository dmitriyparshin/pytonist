list = [1, 4, 2, 9, 5, 7, -7, 0, -45, -10.45]


def sortNum(list):
    global len
    len = len(list)
    for i in range(len):
        for l in range(0, len - i - 1):
            if list[l] > list[l + 1]:
                temp = list[l]
                list[l] = list[l + 1]
                list[l + 1] = temp

sortNum(list)
print(list)