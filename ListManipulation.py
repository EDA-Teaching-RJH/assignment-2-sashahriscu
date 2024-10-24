def main():
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    values.sort()
    values.extend([7, 8])
    
    if 1 in values:
        values.remove(1)
    
    print(values)

main()