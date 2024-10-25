# define principal function
def main():
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# sorting values
    values.sort()
# adding .extend after sort as the instruction is to add the 7 & 8 AFTER the list.
    while 1 in values:
        values.remove(1)
    values.extend([7, 8])
    
    print(values)
# sorted values returned

# call principal function
main()