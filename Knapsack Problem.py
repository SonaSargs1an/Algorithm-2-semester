def knapsack(weights, values, max_capacity):
    num_items = len(weights)
    dp_table = [[0] * (max_capacity + 1) for _ in range(num_items + 1)]

    for item in range(1, num_items + 1):
        for cap in range(max_capacity + 1):
            if weights[item - 1] <= cap:
                dp_table[item][cap] = max(
                    dp_table[item - 1][cap],
                    dp_table[item - 1][cap - weights[item - 1]] + values[item - 1]
                )
            else:
                dp_table[item][cap] = dp_table[item - 1][cap]

    for row in dp_table:
        print(row)

    return dp_table[num_items][max_capacity]

weights = [2, 3, 4, 5]
values = [3, 5, 8, 10]
capacity = 8

print(f'Max value = {knapsack(weights, values, capacity)}') 
