person_1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

person_2 = {
    "name": "Bob",
    "age": 25,
    "city": "San Francisco",
    "occupation": "Designer"
}

person_3 = {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago",
    "occupation": "Architect"
}

people = [person_1,person_2,person_3]

for person in people:
    print(f"info of person : {person['name'].title()}")
    for key, value in person.items():
        print(f"\n{key} is {value}")

print(people)