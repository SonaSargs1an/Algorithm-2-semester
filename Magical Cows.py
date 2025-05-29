def grow_magical_cows(max_cows, num_farms, initial_cows, days):

    dp = [[0] * (max_cows + 1) for _ in range(days + 1)]

    for cow_count in initial_cows:
        dp[0][cow_count] += 1

    for d in range(days):
        for cows in range(1, max_cows + 1):
            farms = dp[d][cows]
            if farms == 0:
                continue

            if cows * 2 <= max_cows:
                dp[d + 1][cows * 2] += farms
            else:
                dp[d + 1][cows] += farms * 2

    for d in range(days + 1):
        total = sum(dp[d])
        print(f"Day {d}: {total} farms")


max_cows = 3
num_farms = 4
initial_cows = [1, 3, 2, 1]
days = 8

grow_magical_cows(max_cows, num_farms, initial_cows, days)
