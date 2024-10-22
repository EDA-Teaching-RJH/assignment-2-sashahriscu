import random

def main():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Original list of numbers:", random_numbers)

    index = 0
    while index < len(random_numbers):
        if random_numbers[index] % 2 == 0:
            random_numbers.pop(i)
        else:
            index += 1

    print("List after removing even numbers:", random_numbers)

main()