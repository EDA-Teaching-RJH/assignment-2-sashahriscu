import random
# define principal function
def main():
# generating range of numbers
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Numbers list :", random_numbers)

    index = 0
    while index < len(random_numbers):
# modulo %2 to distinguish even numbers
        if random_numbers[index]%2 == 0:
            random_numbers.pop(index)
# .pop removes the item at the specified index
        else:
            index += 1
    print("After removing even numbers :", random_numbers)
# return result of removing even numbers from the list

# call principal function
main()
