cities = {
    "New York": {
        "country": "USA",
        "population": "8.4 million",
        "fact": "Known as the Big Apple."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Home to the busiest pedestrian crossing in the world."
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Famous for the Eiffel Tower."
    }
}

for key ,values in cities.items():
    print(f"Info about : {key}")
    for keyy, value in values.items():
        print(f"\t\t\t\t{keyy.title()} : { value}")