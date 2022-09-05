def challenge_compute(coins, amount):
    memo = [[0 for j in range(amount + 1)] for i in range(len(coins)+1)]
    for j in range(1, len(memo[0])):
        memo[0][j] = float('inf')
    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            if coins[i-1] <= j:
                memo[i][j] = min(memo[i-1][j], memo[i][j-coins[i-1]]+1)
            else:
                memo[i][j] = memo[i-1][j]
    
    return memo[-1][-1] if memo[-1][-1] != float('inf') else -1


if __name__ == '__main__':
    qty = int(input());

    for i in range(qty):
        block_count, wished_length = (int(x) for x in input().split());
        blocks = sorted([int(x) for x in input().split()][:block_count]);

        print(challenge_compute(blocks, wished_length));
