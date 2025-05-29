def count_target_ways(numbers, target_sum):
    total_sum = sum(numbers)
    if abs(target_sum) > total_sum or (target_sum + total_sum) % 2 != 0:
        return 0

    subset_sum = (target_sum + total_sum) // 2
    ways = [0] * (subset_sum + 1)
    ways[0] = 1

    for num in numbers:
        for i in range(subset_sum, num - 1, -1):
            ways[i] += ways[i - num]

    return ways[subset_sum]


numbers = [1, 4, 2, 1, 3]
target_sum = 5

print(count_target_ways(numbers, target_sum))  