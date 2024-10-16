#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to reach exactly n H characters
    using only Copy All and Paste operations.

    Args:
        n (int): The number of H characters needed

    Returns:
        int: The minimum number of operations to reach n H characters, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Loop until n is reduced to 1
    while n > 1:
        # Divide n by the current divisor as long as it's divisible
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

