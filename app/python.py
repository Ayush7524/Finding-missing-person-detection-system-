def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_up_to(limit):
    """Find all prime numbers up to the given limit."""
    prime_numbers = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def main():
    # Example usage
    limit = int(input("Enter the upper limit to find prime numbers: "))
    primes = find_primes_up_to(limit)
    print(f"Prime numbers up to {limit} are:")
    print(primes)

if __name__ == "__main__":
    main()
