#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    Args:
        x (int): The number of rounds.
        nums (List[int]): List of integers representing the
        upper bound for each round.
    Returns:
        str: Name of the player that won the most rounds
        ("Maria" or "Ben"). If there's a tie, return None.
    """
    if not nums or x < 1:
        return None
    maria_wins = 0
    ben_wins = 0
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    for n in nums:
        primes_count = sum(sieve[:n + 1])
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
