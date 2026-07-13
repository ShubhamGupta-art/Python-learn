# List of dictionaries containing people and their favorite languages
favorite_languages = {
    'Alice': 'Python',
    'Bob': 'JavaScript',
    'Charlie': 'Ruby',
    'Diana': 'C++'
}

# List of people who haven't taken the poll
people_to_poll = ['Alice', 'Eve', 'Frank', 'Bob', 'Grace']

for person in people_to_poll:
    if person not in favorite_languages:
        print(f"{person.title()} take the poll, Bro!")
    else:
        print(f"{person.title()} thanks for taking the poll")