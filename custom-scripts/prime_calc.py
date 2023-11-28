"""module for a lab challenge"""
from math import sqrt

def is_prime_number(number: int) -> bool:
    """function to calculate prime numbers"""
    if number < 2:
        return False
    max_range = sqrt(number)
    i = 2
    while i <= max_range:
        if number % i == 0:
            return False
        i += 1
    return True

def write_prime_numbers(filename: str) -> None:
    """to write the prime numbers in a file in the current directory"""
    prime_numbers = ""
    for i in range(0, 250):
        if is_prime_number(i):
            prime_numbers += str(i) + " "
    try:
        with open(filename, "w", encoding="utf-8") as result_file:
            result_file.write(prime_numbers)
    except FileNotFoundError:
        print(f"could not save the results in {filename}")

write_prime_numbers("results.txt")
