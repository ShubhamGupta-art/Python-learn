favorite_numbers = {
    'Alice': [7, 14],
    'Bob': [42, 84],
    'Charlie': [3, 6, 9],
    'Diana': [15, 30],
    'Eve': [9, 18, 27]
}

for key,value in favorite_numbers.items():
    print(f"favorite number of {key} is :")
    for num in value:
        print(f"\t\t\t\t{num}")