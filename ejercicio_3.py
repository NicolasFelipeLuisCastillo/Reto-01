numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def is_prime(numbers):
    primes: list = []

    # To avoid checking 1 as a prime number
    if 1 in numbers:
        numbers.remove(1)

    # Check each number in the list
    for number in numbers:
        # Check if the number is prime
        for dividers in range(2, number):
            if number % dividers == 0:
                break
        else:
            primes.append(number)

    print(f"The prime numbers are: {primes}")


is_prime(numbers)

# Explanation:

# The list of numbers is taken and 1 is removed if it is present. 
# Each number is checked to see if it is prime by testing divisibility from 2 to the number minus one. 
# If a number is found to be divisible, it is not prime and the loop breaks. If no divisors are found, 
# the number is added to the list of primes, which is then printed.