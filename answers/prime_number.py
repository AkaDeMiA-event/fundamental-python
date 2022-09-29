def main():
    list = [2]
    for i in range(3, 1000, 2):
        flag = True
        for n in list:
            if i % n == 0:
                flag = False
                break
        if flag:
            list.append(i)
    print(list)

main()


def main2():
    primary_list = []
    num_range = range(2, 1001)
    for num in num_range:
        if num == 2:
            primary_list.append(num)
            continue
        flag = True
        for primary_num in primary_list:
            if num % primary_num == 0:
                flag = False
                break
        if flag:
            primary_list.append(num)
    print(primary_list)

main2()