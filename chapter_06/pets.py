# Define dictionaries for different pets
dog = {
    'name': 'Buddy',
    'animal_type': 'dog',
    'owner': 'Alice',
    'age': 3
}

cat = {
    'name': 'Whiskers',
    'animal_type': 'cat',
    'owner': 'Bob',
    'age': 2
}

parrot = {
    'name': 'Polly',
    'animal_type': 'parrot',
    'owner': 'Charlie',
    'age': 5
}

rabbit = {
    'name': 'Thumper',
    'animal_type': 'rabbit',
    'owner': 'Diana',
    'age': 1
}

# List of pets
pets = [dog, cat, parrot, rabbit]

# Print each pet's information
for pet in pets:
    for key ,value in pet.items():
        print(f"pet {key} {value}")
        # print(f"pet type {pet['name']}")
        # print(f"pet owner {pet['name']}")
        # print(f"pet age {pet['name']}")
        
# Loop through the list and print everything about each pet
for pet in pets:
    print(f"\nHere's what I know about {pet['name']}:")
    print(f"\tAnimal Type: {pet['animal_type'].title()}")
    print(f"\tOwner's Name: {pet['owner']}")
    print(f"\tAge: {pet['age']} years old")