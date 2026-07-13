# Dictionary to store favorite places
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['London', 'Berlin'],
    'Charlie': ['Sydney']
}

# Print the favorite places
for key ,value in favorite_places.items():
    print(f"{key.title()} favorite places are :")
    for place in value:
        print(f"\t{place}")