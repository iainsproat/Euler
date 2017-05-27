import math

def is_prime(candidate):
    for number in range(2, math.ceil(candidate/2)):
        if candidate % number == 0:
            return False

    return True

def factors(number_to_be_factored):
    for factor_candidate in range(2, math.ceil(number_to_be_factored)): # brute force through all possible factors
        if number_to_be_factored % factor_candidate == 0:
            yield factor_candidate

def prime_factor(number_to_be_factored):
    largest_prime_factor = 1

    for factor in factors(number_to_be_factored):
        if is_prime(factor):
            if factor > largest_prime_factor:
                largest_prime_factor = factor

    return largest_prime_factor

if __name__ == "__main__":
    print(prime_factor(600851475143))
