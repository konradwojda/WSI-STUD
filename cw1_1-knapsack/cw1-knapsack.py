weights = [8, 3, 5, 2]  # waga przedmiotów
max_weight = 9  # maksymalna waga plecaka
values = [16, 8, 9, 6]  # wartość przedmiotów

# weights = [i for i in range(25)]
# max_weight = 9
# values = [i for i in range(25)]

def brute_find(wights, max_weight, values):
    binary = []
    for id in range((2**len(weights))):
        temp_bin = f'{id:04b}'
        binary.append(temp_bin)

    # print(binary)

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
    print("Brute find result (weight, value):")
    print(backpack)
    print(winner)
    return

def heuristic_find(weights, max_weight, values):
    ratios = [values[n]/weights[n] for n in range(len(weights))]
    new_weights = [elem for _, elem in sorted(zip(ratios, weights), reverse=True)]
    new_values = [elem for _, elem in sorted(zip(ratios, values), reverse=True)]
    backpack = []
    id = 0
    while sum(i[0] for i in backpack) <= max_weight:
        backpack.append((new_weights[id], new_values[id]))
        id += 1
    if sum(i[0] for i in backpack) > max_weight:
        backpack.pop()
    print("Heuristic find result (weight, value):")
    print(backpack)
    return


brute_find(weights, max_weight, values)
heuristic_find(weights, max_weight, values)
