def smallest_factor(n):
    for i in range(2,  int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,  int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def main():
    while True:
        print("Select an option:")
        print("1. Find the smallest factor of a number")
        print("2. Find prime numbers within a range")


        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            num = int(input("Enter a number to find its smallest factor: "))
            factor = smallest_factor(num)
            if factor:
                print(f"The smallest factor of {num} is {factor}")
            else:
                print(f"{num} is a prime number.")

        elif choice == '2':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            primes_in_range = get_prime_numbers(start, end)
            print(f"Prime numbers between {start} and {end}: {primes_in_range}")


            break

        else:
            print("Invalid choice. Please enter 1, 2.")

if __name__ == "__main__":
    main()











