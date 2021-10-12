weights = [8, 3, 5, 2]  # waga przedmiotów
max_weight = 9  # maksymalna waga plecaka
values = [16, 8, 9, 6]  # wartość przedmiotów


def brute_find(wights, max_weight, values):
    binary = []
    for id in range((2**len(weights))):
        temp_bin = f'{id:04b}'
        binary.append(temp_bin)

    print(binary)

    backpack = []
    temp_backpack = []
    winner = ''
    for num in binary:
        for id in range(len(num)):
            if num[id] == '1':
                item = (weights[id], values[id])
                temp_backpack.append(item)
        if sum(i[0] for i in temp_backpack) > max_weight:
            temp_backpack.clear()
        if sum(i[1] for i in temp_backpack) > sum(i[1] for i in backpack):
            backpack.clear()
            winner = num
            for item in temp_backpack:
                backpack.append(item)
        temp_backpack.clear()

    print(backpack)
    print(winner)

brute_find(weights, max_weight, values)
