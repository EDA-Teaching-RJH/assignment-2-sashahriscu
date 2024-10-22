import random
def main():
    numbers = [random.randint(1, 100) for _ in range(10)]
    
    print("Original list of numbers:")
    print(numbers)
    
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            numbers.pop(index)
        else:
            index += 1
    
    print("List after removing even numbers:")
    print(numbers)

main()