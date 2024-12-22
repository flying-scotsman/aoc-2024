from helpers import get_input
from collections import deque, defaultdict

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def step(s):
    s1 = s * 64
    s = mix(s, s1)
    s = prune(s)
    s2 = s // 32
    s = mix(s, s2)
    s = prune(s)
    s3 = s * 2048
    s = mix(s, s3)
    return prune(s)

def get_price(i):
    return int(str(i)[-1])

def part1(input, number_of_steps):
    total_sum = 0
    for i in input:
        result = int(i)
        for _ in range(number_of_steps):
            result = step(result)
        total_sum += result
    print(f'Total sum of {number_of_steps}th secret numbers: {total_sum}')

def part2(input, number_of_steps):
    # I guess the question is how to figure out the optimum across all buyers.
    # For each individual buyer it's simple, but how can we optimize? There are many combinations...
    # Ah, we should keep a dictionary for the whole list of buyers and just sum up, but only
    # sum across buyers, not for each individual buyer.
    changes = deque(maxlen=4)
    total_prices = defaultdict(int)
    for i in input:
        result = int(i)
        buyers_prices = defaultdict(list)
        last_price = get_price(result)
        for _ in range(number_of_steps):
            result = step(result)
            price = get_price(result)
            changes.append(price - last_price)
            last_price = price
            if len(changes) < 4:
                continue
            # I'm only allowed to look at the first occurrence. So I have
            # to keep all the values and then add the first occurrence of each
            # one to the total prices
            buyers_prices[tuple(changes)].append(price)
        for k, v in buyers_prices.items():
            total_prices[k] += v[0]
    print(f'Maximum number of bananas is {max(total_prices.values())} at changes {max(total_prices, key=total_prices.get)}')

input = get_input('inputs/22.txt')
part2(input, 2000)
