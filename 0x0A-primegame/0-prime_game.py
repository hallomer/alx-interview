#!/usr/bin/python3
"""Prime numbers."""


def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]


def isWinner(x, nums):
    """Determine the winner."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """Simulate a single game."""
        game_nums = set(range(1, n + 1))
        turn = 0

        while True:
            available_primes = [p for p in primes if p in game_nums]
            if not available_primes:
                return 'Ben' if turn == 0 else 'Maria'

            prime = available_primes[0]
            multiples_to_remove = set(range(prime, n + 1, prime))
            game_nums -= multiples_to_remove
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
